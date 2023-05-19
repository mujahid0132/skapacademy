window.scrollTo({
  top:0
})
function submit() {
  let checkoutform = document.getElementById("checkoutform")
  var formData = new FormData(checkoutform);
  let products = localStorage.getItem("cart")
  formData.append('products', products);
  $.ajax({
    url: checkoutform.action,
    type: checkoutform.method,
    data: formData,
    processData: false,
    contentType: false,
    success: function () {
      localStorage.removeItem("cart")
      window.location = "/"
    },
    error: function () {
    }
  });
}
document.querySelectorAll(".alpha").forEach((input) => {
  input.addEventListener("input", function () {
    const aplhabetsonly = /^[a-zA-Z]+$/;
    if (!aplhabetsonly.test(input.value)) {
      input.value = input.value.replace(/[^a-zA-Z]+/g, "");
    }
  });
});
var cleave = new Cleave("#phone_no", {
  blocks: [4, 7],
  numericOnly: true,
});
let firstErrorInput;
const form = document.forms.checkoutform;
const emailInput = form.elements.email;
const phoneNoInput = form.elements.phone_no;
const firstNameInput = form.elements.first_name;
const lastNameInput = form.elements.last_name;
const addressInput = form.elements.address;
const cityInput = form.elements.city;
const postalCodeInput = form.elements.postal_code;
const cfsb = document.getElementById("cfsb")
const phoneNoRegex = /^03[0-9]{2} [0-9]{7,11}$/;
form.addEventListener('submit', validate);
cfsb.addEventListener('click', validate);
function validate(event) {
  event.preventDefault();
  resetErrors();
  let valid = true
  if (!emailInput.value.trim() || !emailInput.checkValidity()) {
    setError(emailInput, 'Please enter a valid email address');
    valid = false
  }
  if (!phoneNoRegex.test(phoneNoInput.value.trim())) {
    setError(phoneNoInput, 'Please enter a valid Pakistani phone number');
    valid = false
  }
  if (!firstNameInput.value.trim()) {
    setError(firstNameInput, 'First Name is required');
    valid = false
  }
  if (!lastNameInput.value.trim()) {
    setError(lastNameInput, 'Last Name is required');
    valid = false
  }
  if (!addressInput.value.trim()) {
    setError(addressInput, 'Address is required');
    valid = false
  }
  if (!cityInput.value.trim()) {
    setError(cityInput, 'City is required');
    valid = false
  }
  if (!postalCodeInput.value.trim()) {
    setError(postalCodeInput, 'Postal Code is required');
    valid = false
  }
  if (valid) { submit() }
  else{
    firstErrorInput.focus();
    firstErrorInput.scrollIntoView({ 
      behavior: 'smooth',
      block: 'center',
  });
  }
  
}

function setError(input, message) {
  input.classList.add('border-red-500');
  const errorMessage = input.nextElementSibling;
  errorMessage.textContent = message;
  if (!firstErrorInput) {
    firstErrorInput = input;
  }
}

function resetErrors() {
  const errorMessages = form.querySelectorAll('.text-sm.text-red-500');
  errorMessages.forEach((message) => (message.textContent = ''));
  firstErrorInput = null;
  const inputs = form.querySelectorAll('input,textarea');
  inputs.forEach((input) => input.classList.remove('border-red-500'));
}