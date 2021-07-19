
// レストラン写真プレビュー表示
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

// 商品写真スワイプ
var swiper = new Swiper('.swiper-container', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  loop: true,
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
  },
});

console.log("Sanity check!");



// サブスクリプションjs
// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // new
  // Event handler
  let submitBtn = document.querySelector("#submitBtn");
  if (submitBtn !== null) {
    submitBtn.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});


function formSwitch() {
      hoge = document.getElementsByName('maker')
      if (hoge[0].checked) {
          // 好きな食べ物が選択されたら下記を実行します
          document.getElementById('freeWord').style.display = "";
          document.getElementById('placeList').style.display = "none";
          document.getElementById('rest_type').style.display = "none";
      } else if (hoge[1].checked) {
          // 好きな場所が選択されたら下記を実行します
          document.getElementById('freeWord').style.display = "none";
          document.getElementById('placeList').style.display = "";
          document.getElementById('rest_type').style.display = "none";
      }else if (hoge[2].checked) {
          // 好きな場所が選択されたら下記を実行します
          document.getElementById('freeWord').style.display = "none";
          document.getElementById('placeList').style.display = "none";
          document.getElementById('rest_type').style.display = "";
      } else {
          document.getElementById('freeWord').style.display = "none";
          document.getElementById('placeList').style.display = "none";
          document.getElementById('rest_type').style.display = "none";
      }
}
window.addEventListener('load', formSwitch());

