function onload(){
    document.getElementById("loading").style.display="none";
}

function csvUpload(){
    event.preventDefault();
    document.getElementById("loading").style.display="block";
    url="http://mccptester.herokuapp.com/lazprice";
    apikey=document.getElementById("apikey").value;

    $.ajax({
      url: url,
      type: 'GET',
      data:{prod: apikey},
      success: function (data) {
        alert("Success. Results file will be downloaded.");
        csv = 'data:text/csv;charset=utf-8,' + encodeURI(data);
        link = document.createElement('a');
        link.setAttribute('href', csv);
        link.setAttribute('download', "download.csv");
        link.click();
        document.getElementById("loading").style.display="none";
      },
      error: function(jqxhr, status, exception) {
          alert("Error.");
          document.getElementById("loading").style.display="none";
      }
    });
}
