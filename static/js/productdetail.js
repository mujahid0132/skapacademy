let quantity = document.getElementById("quantity");
let productname = document.getElementById("productname").textContent;
let producttype = document.getElementById("producttype").textContent;
let productprice = document.getElementById("productprice").textContent;
let productdiscountedprice = document.getElementById("productdiscountedprice").textContent;
let productimg = document.getElementById("productimg").src;
let quantity_val = 1;
function increasequantity() {
  quantity_val += 1;
  quantity.textContent = quantity_val;
  console.log(Object.keys(cart)[0]);
}
function decreasequantity() {
  if (quantity_val > 1) {
    quantity_val -= 1;
    quantity.textContent = quantity_val;
  }
}

let cart = JSON.parse(localStorage.getItem("cart"));
for (k=0;k<Object.keys(cart).length;k++) {
    console.log(Object.keys(cart)[k]);
    if (Object.keys(cart)[k] === productname) {
      addtocartbtn.setAttribute('onclick', 'carttoggle()')
      addtocartbtn.innerHTML = "already in cart,view cart"
      quantitydiv.classList.add("invisible")
      break;
    }
    else {
      addtocartbtn.setAttribute('onclick', 'addtocart()')
      addtocartbtn.innerHTML = "add to cart"
    }
  }
function addtocart() {
  cart[productname] = { //yahan slug rkhna h,img
    name: productname,
    type: producttype,
    img: productimg,
    price: productprice,
    discountedprice: productdiscountedprice,
    quantity: quantity_val,
  };
  addtocartbtn.innerHTML = "already in cart,view cart"
  addtocartbtn.setAttribute('onclick', 'carttoggle()')
  quantitydiv.classList.add("hidden")
  localStorage.setItem("cart", JSON.stringify(cart));
  cartchanger()
}
