let details = document.forms["details"];
let confirmdetails = document.getElementById("confirmdetails")
let productsincart = document.getElementById("productsincart")
let paymentdiv = document.getElementById("paymentdiv")
let continuebtn = document.getElementById("continuebtn")
let completeorder = document.getElementById("completeorder")
let productarray = new Array;
let quantityarray = new Array;
let prod = document.getElementById("product")
let quan = document.getElementById("quantity")
function submit() {
  prod.setAttribute("value",productarray)
  quan.setAttribute("value",quantityarray)
  localStorage.removeItem("cart")
  details.submit();
}
function detailsvalidate() {
    let valid = true
    for (x = 0 ; x<=6 ;x++) {
      if (!details.elements[x].checkValidity()) {
        details.elements[x].nextElementSibling.innerHTML = details.elements[x].validationMessage;
        console.log("not valid");
        valid = false
      } else {
        details.elements[x].nextElementSibling.innerHTML = '';
        console.log("valid");
      }
    }
    if (valid) {
      confirmdetails.classList.remove("hidden")
      confirmdetails.firstElementChild.children[1].innerHTML = details.elements[1].value
      confirmdetails.children[1].children[1].innerHTML = details.elements[4].value
      details.classList.add("hidden");
      confirmdetails.classList.remove("hidden");
      continuebtn.innerHTML = "continue to payment"
      continuebtn.setAttribute("onclick","payment()") 
    }
  }
  function payment() {
    prod.setAttribute("value",`[${productarray}]`)
  quan.setAttribute("value",`[${quantityarray}]`)
  console.log(prod);
  console.log(quan);
    confirmdetails.classList.add("hidden");
    continuebtn.classList.add("hidden");
    paymentdiv.classList.remove("hidden");
    completeorder.classList.remove("hidden");
  }
let cartchk = JSON.parse(localStorage.getItem("cart"))
function productsvalidator() {
  if (productsincart.childElementCount < Object.keys(cartchk).length) {
    let errormessage = document.createElement("div")
    errormessage.innerHTML = "Some items in your cart are not available"
    productsincart.appendChild(errormessage)
    return false;
  }
  else{
    return true;
  }
}
function quantityadder() {
  let maxiteration = 0;
  productsvalidator()===true?maxiteration = productsincart.childElementCount:maxiteration = productsincart.childElementCount - 1
  for (let index = 1; index <= maxiteration; index++) {
    let n = productsincart.children[index-1].children[0].innerHTML
    console.log(n);
    let m = n.replace(/ /g, "-")
    console.log(m);
    let quant = document.getElementById(`quantity${m}`)
    quant.innerHTML = cartchk[n].quantity
    productarray.push(n)
    quantityarray.push(quant.innerHTML)
  }
  console.log(quantityarray);
  console.log(productarray);
}
quantityadder()