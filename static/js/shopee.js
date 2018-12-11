function onload(){
    document.getElementById("loading").style.display="none";
}

function shopeeRedirect(){
    url="https://mccptester.herokuapp.com/shopeeurl";
    $.ajax({
      url: url,
      type: 'GET',
      success: function (data) {
        var jidraw=JSON.parse(data);
        var url=jidraw['url'];
        if (confirm('You will be redirected to Shopee for authentication.')) {
            window.location.href = url;
        }
        document.getElementById("loading").style.display="none";
      },
      error: function(jqxhr, status, exception) {
          alert('Exception:', exception);
          document.getElementById("loading").style.display="none";
      }
    });
}
