let highlight_js = document.createElement("script")
highlight_js.type = "text/javascript"
highlight_js.setAttribute("src", "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js")
document.head.appendChild(highlight_js)
highlight_js.addEventListener("load", function() {
let quill_js = document.createElement("script")
quill_js.setAttribute("src", "https://cdn.quilljs.com/1.3.6/quill.js")
document.head.appendChild(quill_js)
let quill_css = document.createElement("link")
quill_css.setAttribute("href", "https://cdn.quilljs.com/1.3.6/quill.snow.css")
quill_css.setAttribute("rel", "stylesheet")
document.head.appendChild(quill_css)
quill_js.addEventListener("load", function() {
    var quill = new Quill('#id_description', {
        theme: 'snow',        
      });
  })
  })
  