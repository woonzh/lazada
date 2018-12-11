function onload(){
    document.getElementById("loading").style.display="none";
}

function cloneTable(count){
  var div = document.getElementById('duplicate');
  var clone = div.cloneNode(true);

  var but = clone.getElementsByTagName("button")[0];
  but.innerHTML="testing";
  but.setAttribute('data-target','#demo'+String(count));

  var divc = clone.getElementsByTagName("div")[0];
  divc.setAttribute("id", "demo"+String(count));

  var main=document.getElementById('dup main');
  main.appendChild(clone);

}

$('.clone').click(function () {
  alert("clicked");
  cloneTable(1);
});

function getShipments(){
  document.getElementById("loading").style.display="block";
  var orderno=document.getElementById("orderno").value;
  alert(orderno);
  url='https://mccptester.herokuapp.com/deliverycheck';
  $.ajax({
    url: url,
    type: 'GET',
    data: {
      increment_id:orderno
      },
    success: function (data) {
      alert(data);
      document.getElementById("loading").style.display="none";
    },
    error: function(data) {
        alert(data);
        document.getElementById("loading").style.display="none";
    }
  });
}
