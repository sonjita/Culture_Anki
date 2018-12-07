
var dialog = document.getElementById("dialog");
dialog.style.display = "none";
add_botton = document.getElementById("add");
//document.getElementById("lang_selector").value = "none";

function toggleVisibility() { //if one of the questions not answered, flash "please answer all the questions"
    dialog.style.display = "block";
    add_botton.style.display = "none"
}

function cancel(evt) {
    evt.preventDefault()
    dialog.style.display = "none";
    add_botton.style.display = "block"
}
