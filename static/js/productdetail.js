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
}
function decreasequantity() {
  if (quantity_val > 1) {
    quantity_val -= 1;
    quantity.textContent = quantity_val;
  }
}
function buttonchanger() {
  let cart = JSON.parse(localStorage.getItem("cart"));
  if (Object.keys(cart).includes(productname)) {
  addtocartbtn.setAttribute('onclick', 'carttoggle()')
  addtocartbtn.innerHTML = "already in cart,view cart"
  quantitydiv.classList.add("hidden")
}
else {
  addtocartbtn.setAttribute('onclick', 'addtocart()')
  addtocartbtn.innerHTML = "add to cart"
  quantitydiv.classList.remove("hidden")
}
}
buttonchanger()
function addtocart() {
  let cart = JSON.parse(localStorage.getItem("cart"));
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
