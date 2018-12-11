var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

function onload(){
  url="https://mccptester.herokuapp.com/accounts";
  $.ajax({
    url: url,
    type: 'GET',
    success: function (data) {
      var accts = JSON.parse(data);
      var accountList = document.getElementById("account");
      for (var i in accts){
        var acct=accts[i];
        var sellerid=acct['seller_id'];
        var name=acct['acct_name'];
        var option = document.createElement("option");
        option.text = name;
        option.value = sellerid;
        accountList.add(option);
      }
      document.getElementById("loading").style.display="none";
    },
    error: function(jqxhr, status, exception) {
        alert('Exception:', exception);
        document.getElementById("loading").style.display="none";
    }
  });
}

function cloneTable(){
  var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
  $TABLE.find('table').append($clone);
}

$('.table-allsync').click(function () {
  var r = confirm("Confirm sync inventory?");
  if (r==true){
    document.getElementById("loading").style.display="block";
    var acct=document.getElementById("account").value;
    var name=document.getElementById("account").innerHTML;
    url="https://mccptester.herokuapp.com/inventory";
    $.ajax({
      url: url,
      type: 'GET',
      data:{
        sellerid:acct,
        purpose:"recon",
        ctype:"seller"
      },
      success: function (data) {
        var jidraw=JSON.parse(data);
        var jid=jidraw['jobid'];
        alert("Recon Job for this account is underway in the background. Refresh again 5 mins later.")
        document.getElementById("loading").style.display="none";
      },
      error: function(jqxhr, status, exception) {
          alert('Exception:', exception);
          document.getElementById("loading").style.display="none";
      }
    });
  }
});

$('.table-sync').click(function () {
  document.getElementById("loading").style.display="block";
  var acct=document.getElementById("account").value;
  var imssku=$(this).closest("tr").find(".imssku").text();
  var imsinven=$(this).closest("tr").find(".imsinven");
  var mccpinven=$(this).closest("tr").find(".mccpinven");
  url="https://mccptester.herokuapp.com/inventory";
  $.ajax({
    url: url,
    type: 'GET',
    data: {
      purpose: "recon",
      ctype:"sku",
      imssku:imssku,
      sellerid:acct
    },
    success: function (data) {
      var jidraw=JSON.parse(data);
      var result=jidraw['result'];
      var qty=jidraw['qty'];
      imsinven.html(qty);
      mccpinven.html(qty)
      document.getElementById("loading").style.display="none";
    },
    error: function(data) {
        alert(data);
        document.getElementById("loading").style.display="none";
    }
  });
});

function updateTable(result,name){
  var accts=result['result'];
  var tableRef = document.getElementById("acctTable");
  rowCount=2;
  for (var i in accts){
    var acctSet=accts[i];
    cloneTable();
    var x=tableRef.rows;
    var y=x[rowCount].cells;
    var colCount=1;
    y[0].innerHTML = name;
    for (var j in acctSet){
      y[colCount].innerHTML = acctSet[j];
      colCount=colCount+1;
    }
    rowCount=rowCount+1;
    document.getElementById("loading").style.display="none";
  }
}

function getReply(jid, name){
  url="https://mccptester.herokuapp.com/jobreport";
  var succ=false;
  $.ajax({
    url: url,
    type: 'GET',
    data:{
      jobid:jid
    },
    success: function (data) {
      var result=JSON.parse(data);
      var status=result['status'];
      if (status=="Completed"){
        updateTable(result, name)
        document.getElementById("loading").style.display="none";
        return result;
      }else if (status=="failed") {
        alert("Failed in pulling inventory");
        document.getElementById("loading").style.display="none";
        return result
      }
      else{
        return setTimeout(function(){ getReply(jid, name); }, 3000);
      }
    },
    error: function(jqxhr, status, exception) {
        alert('Exception:', exception);
        document.getElementById("loading").style.display="none";
    }
  });
}

function acctChange(){
  document.getElementById("loading").style.display="block";
  var acct=document.getElementById("account").value;
  var name=document.getElementById("account").innerHTML;
  url="https://mccptester.herokuapp.com/inventory";
  $.ajax({
    url: url,
    type: 'GET',
    data:{
      sellerid:acct,
      purpose:"data"
    },
    success: function (data) {
      var jidraw=JSON.parse(data);
      var jid=jidraw['jobid'];
      var timeNeeded=parseFloat(jidraw['time'])*1000;
      var result = setTimeout(function(){ getReply(jid, name); }, timeNeeded);
    },
    error: function(jqxhr, status, exception) {
        alert('Exception:', exception);
        document.getElementById("loading").style.display="none";
    }
  });
}
