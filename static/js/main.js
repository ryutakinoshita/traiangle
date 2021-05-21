function imgPreView(event) {
  var file = event.target.files[0];
  var reader = new FileReader();
  var preview = document.getElementById("preview");
  var previewImage = document.getElementById("previewImage");

  if(previewImage != null) {
    preview.removeChild(previewImage);
  }
  reader.onload = function(event) {
    var img = document.createElement("img");
    img.setAttribute("src", reader.result);
    img.setAttribute("id", "previewImage");
    preview.appendChild(img);
  };

  reader.readAsDataURL(file);
}

var selecterBox = document.getElementById('checkOn');

function formSwitch() {
    check = document.getElementsByClassName('registration_main_radio')
    if (check[1].checked) {
        selecterBox.style.display = "none";

    } else if (check[2].checked) {
        selecterBox.style.display = "none";

    } else {
        selecterBox.style.display = "block";
    }
}
window.addEventListener('load', formSwitch());

function entryChange2(){
    if(document.getElementById('changeSelect')){
    id = document.getElementById('changeSelect').value;
}
}

function restImgPreView(event,targetId) {
  var file = event.target.files[0];
  var reader = new FileReader();
  var preview = document.getElementById(targetId);
  var previewImage = document.getElementById("previewImage-"+targetId);

  if(previewImage != null) {
    preview.removeChild(previewImage);
  }

  reader.onload = function(event) {
     var img = document.createElement("img");
     img.setAttribute("src", reader.result);
     img.setAttribute("id", "previewImage-"+targetId);
     preview.appendChild(img);
  };

  reader.readAsDataURL(file);
}