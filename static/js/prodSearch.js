function onload(){
  alert('test');
  document.getElementById("loading").style.display="none";
}

function clearRows(){
  table=document.getElementById("results");
  alert(table.rows.length);
  while(table.rows.length>2){
    table.deleteRow(2)
  }
}

function displayResults(data){
  var table=document.getElementById("results body");
  while(table.rows.length>1){
    table.deleteRow(1)
  }

  var nodeClone=document.getElementById("clone row");

  data=JSON.parse(data);
  for (var prodName in data){
    var prod=data[prodName];
    for (var i=0; i<prod.length; i++){
      var new_row = nodeClone.cloneNode(true);
      new_row.style.display="";
      new_row.id="";
      var line = prod[i];
      for (var colName in line){
        if (colName=="country"){new_row.cells[5].innerHTML=line[colName];}
        if (colName=="discount"){new_row.cells[3].innerHTML=line[colName];}
        if (colName=="name"){new_row.cells[0].innerHTML=line[colName];}
        if (colName=="original price"){new_row.cells[2].innerHTML=line[colName];}
        if (colName=="reviews"){new_row.cells[4].innerHTML=line[colName];}
        if (colName=="price"){new_row.cells[1].innerHTML=line[colName];}
        /*switch(colName){
          case "country":
            new_row.cells[5].innerHTML=line[colName];
            break;
          case "discount":
            new_row.cells[3].innerHTML=line[colName];
            break;
          case "name":
            new_row.cells[0].innerHTML=line[colName];
            break;
          case "original price":
            new_row.cells[2].innerHTML=line[colName];
            break;
          case "reviews":
            new_row.cells[4].innerHTML=line[colName];
            break;
          case "price":
            new_row.cells[1].innerHTML=line[colName];
            break;*/
        }
        table.append(new_row);
      }
    }
}

function testSearch(){
  alert('test');
  var data={
    'samsung tab':[
      {"name":"test1", "price":"100", "country":"Singapore", "original price": "500", "reviews": "3", "discount":"10"},
      {"name":"test2", "price":"200","country":"Singapore", "original price": "500", "reviews": "3", "discount":"10"},
      {"name":"test3", "price":"300","country":"Singapore", "original price": "500", "reviews": "3", "discount":"10"}
    ]
  };
  displayResults(data);
}

function productSearch(){
  document.getElementById("loading").style.display="block";
  url="http://localhost:8080/product";
  product=document.getElementById("product").value;

  $.ajax({
    url: url,
    type: 'GET',
    data:{product: product},
    success: function (data) {
      displayResults(data);
      document.getElementById("loading").style.display="none";
    },
    error: function(jqxhr, status, exception) {
      alert("Error.");
      document.getElementById("loading").style.display="none";
    }
  });
}
