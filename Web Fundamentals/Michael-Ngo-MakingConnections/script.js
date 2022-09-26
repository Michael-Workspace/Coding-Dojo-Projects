var edits = document.querySelector(".name");


function edit(){
    edits.innerHTML = "Michael Ngo"
}

var request = document.querySelector(".alert")
var connection = document.querySelector(".alert2")


function accept(id){
    var element = document.querySelector(id);
    element.remove();
    request.innerHTML--;
    connection.innerHTML++;
}

function decline(id){
    var element = document.querySelector(id);
    element.remove();
    request.innerHTML--;
    connection.innerHTML--;
}