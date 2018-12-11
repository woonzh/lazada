function onload(){
    document.getElementById("loading").style.display="none";
}

function checkupload(){
    var x = document.getElementById("csv");
    txt = "Select one or more files.";
    if ('files' in x) {
        if (x.files.length == 0) {
            txt = "Select one or more files.";
        } else {
            for (var i = 0; i < x.files.length; i++) {
                txt += "<br><strong>" + (i+1) + ". file</strong><br>";
                var file = x.files[i];
                if ('name' in file) {
                    txt += "name: " + file.name + "<br>";
                }
                if ('size' in file) {
                    txt += "size: " + file.size + " bytes <br>";
                }
            }
        }
    }else {
        if (x.value == "") {
            txt += "Select one or more files.";
        } else {
            txt += "The files property is not supported by your browser!";
            txt  += "<br>The path of the selected file: " + x.value; // If the browser does not support the files property, it will return the path of the selected file instead.
        }
    }
    document.getElementById("result").innerHTML = txt;
}

function csvUpload(){
    event.preventDefault();
    document.getElementById("loading").style.display="block";
    url="http://mccptester.herokuapp.com/orderfile";
    checkupload();
    var fd = new FormData();
    file=document.getElementById("csv").files[0];
    fd.append('data', file);
    apikey=document.getElementById("apikey").value;
    fd.append('apikey', apikey);
    document.getElementById("csv").value="";

    $.ajax({
      url: url,
      type: 'POST',
      processData: false,
      contentType: false,
      cache: false,
      data:fd,
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
