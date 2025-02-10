document.getElementById("watch").addEventListener("click", function(event){
    document.getElementById("myDropdown").classList.add("open");
});

document.getElementById("back_button").addEventListener("click", function(event){
    document.getElementById("myDropdown").classList.remove("open");
});