let cartdiv = document.getElementById("cartdiv");
let carthtml = document.getElementById("carthtml");
let clearcartbtn = document.getElementById("clearcartbtn");
let checkoutbtn = document.getElementById("checkoutbtn");
let addtocartbtn = document.getElementById("addtocartbtn");
let quantitydiv = document.getElementById("quantitydiv");
let emptymsg = document.getElementById("emptymsg");
let csrf = document.getElementsByName('csrfmiddlewaretoken');
let checkoutform = document.getElementsByName('checkoutform');

function cartset() {
    if (localStorage.getItem("cart") === null) {
        localStorage.setItem("cart", JSON.stringify({}));
    }
}
window.onload = function() {
    cartset();
};
function cartchanger() {
    let obj = JSON.parse(localStorage.getItem("cart"))
    let cartnumber = document.getElementById("cartnumber")
    let size = Object.keys(obj).length;
    cartnumber.innerHTML = size
    if (size === 0) {
        emptymsg.classList.remove("hidden")
    }
    if (size > 0) {
        carthtml.innerHTML = ""
        clearcartbtn.classList.remove("hidden")
        checkoutbtn.classList.remove("hidden")
    }
    for (let k = 1; k <= size; k++) {
        let box = document.createElement("div")
        // let img = document.createElement("img")
        // img.setAttribute('src',obj[Object.keys(obj)[k-1]].img);
        // let quantity = document.createElement("div")
        // quantity.innerHTML = `<button onclick="cartquantitychange(${k},'-')">-</button>
        // <span id="cartquantity${k}">${obj[Object.keys(obj)[k-1]].quantity}</span>
        // <button onclick="cartquantitychange(${k},'+')">+</button>`
        // img.classList.add("aspect-square")
        // box.appendChild(quantity)
        box.innerHTML = `
        <div class="box">
		<img src="${obj[Object.keys(obj)[k-1]].img}">
		<div class="details">
			<span class="title">Title</span>
			<span class="subtitle">Subtitle</span>
			<span class="category">Category</span>
            <div class="quantity">
                <button onclick="cartquantitychange(${k},'-')">-</button>
                <div id="cartquantity${k}">${obj[Object.keys(obj)[k-1]].quantity}</div>
                <button onclick="cartquantitychange(${k},'+')">+</button>
                </div>
                </div>
                </div>
                `;
                carthtml.appendChild(box)
    }
}
cartchanger()
function carttoggle() {
    cartdiv.classList.toggle("hidden")
} 
function clearcart() {
    carthtml.innerHTML = "Your cart is empty"
    cartnumber.innerHTML = 0
    clearcartbtn.classList.add("hidden")
    checkoutbtn.classList.add("hidden")
    localStorage.setItem("cart", JSON.stringify({}));
    if (addtocartbtn !== null) {
        quantitydiv.classList.remove("hidden")
        addtocartbtn.setAttribute('onclick', 'addtocart()')
        addtocartbtn.innerHTML = "add to cart"
    }
    location.reload()
} 
function checkout() {
    let obj = JSON.parse(localStorage.getItem("cart"))
    let keys = Object.keys(obj);
    let keysString = keys.join("_");
    $.ajax({
        type: "POST",
        url: "/shop/checkout/",
        data: {'products': keysString,
        'csrfmiddlewaretoken':csrf[0].value},
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
