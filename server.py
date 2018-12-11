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
import lazada

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html')
    
class crawlLazada(Resource):
    def get(self):
        prod=request.args.get("product", type=str, default="marshall in-ear")
        print("testworker start")
        q=Queue(connection=conn)
        job=q.enqueue(lazada.getProduct, prod)
        print("testworker ends")
        return str(job.id)
    
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

api.add_resource(crawlLazada, '/testworker')
api.add_resource(Failedworkers, '/failedworkers')
api.add_resource(GetJobReport, '/jobreport')


if __name__ == '__main__':
     app.run(debug=True)