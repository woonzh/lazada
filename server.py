# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:13:11 2018

@author: ASUS
"""

import flask
from flask import Flask, request, make_response, render_template, redirect
from flask_cors import CORS
from flask_restful import Resource, Api
import json
import redis
from rq import Connection, get_failed_queue, Queue, get_current_job
from rq.job import Job
from worker import conn
import os
import executor

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def mainPage():
    return redirect("http://localhost:8080/prodsearch", code=302)

@app.route('/prodsearch')
def prodSearch():
    return render_template('prodSearch.html')

@app.route('/popular')
def popular():
    return render_template('popular.html')

class CheckLazadaPrice(Resource):
    def get(self):
        prod=request.args.get("product", type=str)
        print(prod)
        df=executor.getProduct([prod], 'json')
        print(df)
        
        resp = flask.Response(json.dumps(df))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    
class GetHrefs(Resource):
    def get(self):
        df=executor.getHrefs('json')
        print(df)
        resp = flask.Response(json.dumps(df))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    
class GetSubCat(Resource):
    def get(self):
        url=request.args.get("url", type=str)
        df=executor.getSubCat(url)
        print(df)
        
        resp = make_response(df.to_csv(header=True, index=False))
        resp.headers["Content-Disposition"] = "attachment; filename=error_reports.csv"
        resp.headers["Content-Type"] = "text/csv"
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Methods']= 'GET,PUT,POST,DELETE,OPTIONS'
        return resp
    
class Failedworkers(Resource):
    def get(self):
        redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
        conn = redis.from_url(redis_url)
        ret={}
        with Connection(conn):
            failed_jobs= get_failed_queue()
            print(failed_jobs.jobs)
            ret['failed jobs']=failed_jobs.jobs
        
        resp = flask.Response(json.dumps(ret))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        print("header success")
        return resp
    
class GetJobReport(Resource):
    def get(self):
        jobid = request.args.get("jobid" ,type = str, default="")
        redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
        conn = redis.from_url(redis_url)
        ret={}
        with Connection(conn):
            job = Job.fetch(jobid,conn)
            if job.is_finished:
                ret['status']='Completed'
                ret['result']=job.return_value
            elif job.is_queued:
                ret['status']='in-queue'
            elif job.is_started:
                ret['status']='waiting'
            elif job.is_failed:
                ret['status']='failed'
        
        resp = flask.Response(json.dumps(ret))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        print("header success")
        return resp
    
class test(Resource):
    def get(self):
        a={'data':'test'}
        
        resp = flask.Response(json.dumps(a))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        print("header success")
        return resp

api.add_resource(Failedworkers, '/failedworkers')
api.add_resource(GetJobReport, '/jobreport')
api.add_resource(CheckLazadaPrice, '/product')
api.add_resource(test, '/test')
api.add_resource(GetHrefs, '/hrefs')
api.add_resource(GetSubCat, '/subcat')


if __name__ == '__main__':
#    port = int(os.environ.get('PORT', 8080))
#    app.run(debug=True, host='localhost', port=8080)
    app.run(debug=True, host='0.0.0.0', port=8080)