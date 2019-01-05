var results=''
var mainOption=document.getElementById('mainCat')
var secondaryOption=document.getElementById('secCat')

function updateMainCat(){
  for (i=0; i<results.length;i++){
    var option=document.createElement("option");
    option.text=results[i]['name'];
    option.value=i;
    mainOption.add(option);
  }
}

function removeOptions(ele){
  do{
    ele.remove(1);
  }while(ele.length>1);
}

function updateSubCat(){
  mainCat=Number(mainOption.options[mainOption.selectedIndex].value);
  catSelected=results[mainCat];
  details=catSelected['subcats'];
  removeOptions(secondaryOption);
  for (i=0; i<details.length; i++){
    var option=document.createElement("option");
    option.text=details[i]['name']
    option.value=details[i]['href']
    secondaryOption.add(option);
  }
}

function getCategoryResults(){
  document.getElementById("loading").style.display="block";
  url='http://localhost:8080/subcat'
  $.ajax({
    url: url,
    type: 'GET',
    data: {url:secondaryOption.options[secondaryOption.selectedIndex].value},
    success: function (data) {
      alert("Success. Results file will be downloaded.");
      csv = 'data:text/csv;charset=utf-8,' + encodeURI(data);
      link = document.createElement('a');
      link.setAttribute('href', csv);
      link.setAttribute('download', "download.csv");
      link.click();;
      document.getElementById("loading").style.display="none";
    },
    error: function(jqxhr, status, exception) {
      alert("Error.");
      document.getElementById("loading").style.display="none";
    }
  });
}

function onload(){
  //document.getElementById("loading").style.display="none";
  url='http://localhost:8080/hrefs'
  $.ajax({
    url: url,
    type: 'GET',
    success: function (data) {
      results=JSON.parse(data);
      updateMainCat();
      document.getElementById("loading").style.display="none";
    },
    error: function(jqxhr, status, exception) {
      alert("Error.");
      document.getElementById("loading").style.display="none";
    }
  });
}
