let cartdiv = document.getElementById("cartdiv");
let carthtml = document.getElementById("carthtml");
let clearcartbtn = document.getElementById("clearcartbtn");
let checkoutbtn = document.getElementById("checkoutbtn");
let addtocartbtn = document.getElementById("addtocartbtn");
let quantitydiv = document.getElementById("quantitydiv");
let checkoutform = document.forms["checkoutform"];
let csrf = checkoutform[0]

function cartset() {
    if (localStorage.getItem("cart") === null) {
        localStorage.setItem("cart", JSON.stringify({}));
    }
}
window.onload = function() {
    cartset();
};
function cartchanger(sizeminus = 0) {
    let obj = JSON.parse(localStorage.getItem("cart"))
    let cartnumber = document.getElementById("cartnumber")
    let size = Object.keys(obj).length-sizeminus;
    cartnumber.innerHTML = size
    if (size === 0) {
        clearcart()
    }
    if (size > 0) {
        carthtml.innerHTML = ""
        carthtml.classList.remove("justify-center")
        clearcartbtn.classList.remove("hidden")
        checkoutbtn.classList.remove("hidden")
    }
    for (let k = 1; k <= size; k++) {
        let box = document.createElement("div")
        box.classList.add("cart-item")
        box.innerHTML = `
		<img src="${obj[Object.keys(obj)[k-1]].img}">
		<div class="details">
			<span class="name">${obj[Object.keys(obj)[k-1]].name}</span>
			<span class="sku">${obj[Object.keys(obj)[k-1]].type}</span>
            <div class="flex space-x-2 py-4">
                <span class="font-semibold text-xl" >Rs. </span>
                <div class="flex flex-col -space-y-2">
                <span class="line-through text-xs" id="productprice">${obj[Object.keys(obj)[k-1]].price}</span>
                <span class="font-semibold text-sm" id="productdiscountedprice">${obj[Object.keys(obj)[k-1]].discountedprice}</span>
    </div>
  </div>
                <div class="flex">
                <div class="flex quantity">
                <button onclick="cartquantitychange(${k},'-')">-</button>
                <div id="cartquantity${k}">${obj[Object.keys(obj)[k-1]].quantity}</div>
                <button onclick="cartquantitychange(${k},'+')">+</button>
                </div>
                <button class="underline" onclick="removefromcart('${obj[Object.keys(obj)[k-1]].name}')">Remove</button>
                </div>
                </div>
                `;
                carthtml.appendChild(box)
    }
}
cartchanger()
function carttoggle() {
    let currentpos = cartdiv.style.right;
      if (currentpos == "0px") {
        cartdiv.style.right = "-100%"
      }
      else{
          cartdiv.style.right = "0"
        }
} 
function clearcart() {
    carthtml.innerHTML = "Your cart is empty"
    cartnumber.innerHTML = 0
    clearcartbtn.classList.add("hidden")
    checkoutbtn.classList.add("hidden")
    localStorage.setItem("cart", JSON.stringify({}));
    if (addtocartbtn) {
        buttonchanger()
    }
} 
function checkout() {
    let products = localStorage.getItem("cart");
    $.ajax({
        type: "POST",
        url: "/shop/checkout/",
        data: {'products': products,
        'csrfmiddlewaretoken':csrf.value,
    },
        success: function(html) {
            var newUrl = "/shop/checkout/";
            window.history.replaceState({}, "", newUrl);
            document.getElementsByTagName("html")[0].innerHTML = html;
            let checkoutscript = document.createElement("script")
            checkoutscript.setAttribute("src" , "/static/js/checkout.js")
            document.body.appendChild(checkoutscript)
        }
    });
} 
function cartquantitychange(product , operator) {
    let obj = JSON.parse(localStorage.getItem("cart"))
    let cartquantity = document.getElementById(`cartquantity${product}`)
    if (operator === "+") {
        obj[Object.keys(obj)[product-1]] = {
            name: obj[Object.keys(obj)[product-1]].name,
            type: obj[Object.keys(obj)[product-1]].type,
            img: obj[Object.keys(obj)[product-1]].img,
            price: obj[Object.keys(obj)[product-1]].price,
            discountedprice: obj[Object.keys(obj)[product-1]].discountedprice,
            quantity: obj[Object.keys(obj)[product-1]].quantity += 1,
        };
        cartquantity.innerHTML = Number(cartquantity.innerHTML) + 1
    } if(operator === "-" && obj[Object.keys(obj)[product-1]].quantity>1){
        obj[Object.keys(obj)[product-1]] = {
            name: obj[Object.keys(obj)[product-1]].name,
            type: obj[Object.keys(obj)[product-1]].type,
            img: obj[Object.keys(obj)[product-1]].img,
            price: obj[Object.keys(obj)[product-1]].price,
            discountedprice: obj[Object.keys(obj)[product-1]].discountedprice,
            quantity: obj[Object.keys(obj)[product-1]].quantity -= 1,
        };
        cartquantity.innerHTML = Number(cartquantity.innerHTML) - 1
        
    }
    localStorage.setItem("cart", JSON.stringify(obj));
}
function removefromcart(product) {
    let cart = JSON.parse(localStorage.getItem("cart"))
    delete cart[product]; 
    let cartlength = Object.keys(cart).length;
    if (cartlength === 0) {
        
    }
    cartchanger(sizeminus = 1)
    localStorage.setItem("cart", JSON.stringify(cart));
    if (addtocartbtn) {
        buttonchanger()
    }
    
}
