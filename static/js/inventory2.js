function onload(){
    document.getElementById("loading").style.display="none";
}

function csvUpload(){
    event.preventDefault();
    document.getElementById("loading").style.display="block";
    url="http://mccptester.herokuapp.com/inventorycheck";
    var fd = new FormData();
    apikey=document.getElementById("apikey").value;
    fd.append('apikey', apikey);
    sku=document.getElementById("sku").value;
    fd.append('sku', sku);

    $.ajax({
      url: url,
      type: 'POST',
      processData: false,
      contentType: false,
      cache: false,
      data:fd,
      success: function (data) {
        var tem=JSON.parse(data);
        var qty=tem['qty'];
        skufield=document.getElementById("result2");
        skufield.innerHTML="Inventory: " + String(qty);
        document.getElementById("loading").style.display="none";
      },
      error: function(jqxhr, status, exception) {
          skufield=document.getElementById("sku");
          skufield.innerHTML="Inventory: ";
          alert("Error.");
          document.getElementById("loading").style.display="none";
      }
    });
}
