
// var dialog = document.getElementById("dialog");
// dialog.style.display = "none";
var dialogs = document.getElementsByName("dialog");
dialogs.forEach(function(element){
    element.style.display = "none"
})

add_botton = document.getElementById("add");
//document.getElementById("lang_selector").value = "none";

function toggleVisibility(dialog_name) { //if one of the questions not answered, flash "please answer all the questions"
    console.log(dialog_name)
    dialog = document.getElementById(dialog_name)
    dialog.style.display = "block";

    add_botton.style.display = "none"
}

function cancel() {
    dialog.style.display = "none";
    add_botton.style.display = "block";
    let select_fields = document.getElementsByName('dialog_select');
    let text_fields = document.getElementsByName('dialog_input');
    
    select_fields.forEach(function(element) {
        element.value = "none"
    })

    text_fields.forEach(function(element){
        element.value="";
    })

    var inner = document.getElementById('inner_dialog');
    inner.style.display = "none";
}

