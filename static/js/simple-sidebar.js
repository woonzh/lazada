var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

function validateAcctFields(){
  var fields = document.getElementsByClassName("fields");
  var i;
  var check = true;
  for (i = 0; i < fields.length; i++) {
      var tem= fields[i].value;
      if (fields[i].value==""){
        fields[i].style.backgroundColor = "red";
        check=false;
      }
  }

  if (!check){
    alert("Please fill in all fields in red to create an account.");
    fields[0].focus();
  }

  return check;
}

function createAccount(e){
  if (validateAcctFields()){
    url='https://shopifyorder.herokuapp.com/createAccount';
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var apikey = document.getElementById("apikey").value;
    var password = document.getElementById("password").value;
    var shared = document.getElementById("sharedsecret").value;

    $.ajax({
      url: url,
      type: 'GET',
      data: {name:name,email:email,apikey:apikey,password:password,sharedsecret:shared},
      success: function (data) {
        alert(data);
        location.reload();
      },
      error: function(data){
        alert(data);
        location.reload();
      }
    });
  }
}

function onload(){
  url="https://mccptester.herokuapp.com/accountdetails"
  $.ajax({
    url: url,
    type: 'GET',
    success: function (data) {
      var accts = JSON.parse(data);
      var tableRef = document.getElementById("acctTable");
      rowCount=2;
      for (var i in accts){
        var acctSet=accts[i];
        cloneTable();
        var x=tableRef.rows;
        var y=x[rowCount].cells;
        var colCount=0;
        for (var j in acctSet){
          y[colCount].innerHTML = acctSet[j];
          colCount=colCount+1;
        }
        rowCount=rowCount+1;
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

$('.table-up').click(function(){
  alert("still works in progress")
  /*document.getElementById("loading").style.display="block";
  var email=$(this).closest("tr").find(".email").text();
  var name=$(this).closest("tr").find(".acctname").text();
  var api=$(this).closest("tr").find(".api").text();
  var password=$(this).closest("tr").find(".password").text();
  var shared=$(this).closest("tr").find(".sharedsecret").text();
  url='https://shopifyorder.herokuapp.com/editaccount';
  $.ajax({
    url: url,
    type: 'GET',
    data: {
      name:name,
      email:email,
      apikey:api,
      password:password,
      sharedsecret:shared
      },
    success: function (data) {
      alert(data);
      location.reload();
      document.getElementById("loading").style.display="none";
    },
    error: function(data) {
        alert(data);
        document.getElementById("loading").style.display="none";
    }
  });*/
});

$('.table-remove').click(function () {
  alert("still works in progress")
  /*document.getElementById("loading").style.display="block";
  var x=$(this).closest("tr").find(".acctname").text();
  var r = confirm("Confirm delete "+x+"?");
  if (r==true){
    url='https://shopifyorder.herokuapp.com/deleteAccount';
    $.ajax({
      url: url,
      type: 'GET',
      data: {name:x},
      success: function (data) {
        alert(data);
        location.reload();
        document.getElementById("loading").style.display="none";
      },
      error: function(data) {
          alert(data);
          document.getElementById("loading").style.display="none";
      }
    });
  }*/
});

// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$BTN.click(function () {

});
