document.getElementById("personal_data_button").classList.add("active");
document.getElementById("personal").classList.add("active");
document.getElementById("films_page").classList.add("hidden");
count = 0;
document.getElementById("wrap").classList.add("hidden");
document.getElementById("wrap_liked").classList.add("hidden");

document.getElementById("personal_data_button").addEventListener("click", function(){
    document.getElementById("personal_data_button").classList.add("active");
    document.getElementById("personal").classList.add("active");
    document.getElementById("films_button").classList.remove("active");
    document.getElementById("films").classList.remove("active");
    document.getElementById("personal_info").classList.remove("hidden");
    document.getElementById("films_page").classList.add("hidden");
});

document.getElementById("films_button").addEventListener("click", function(){
    document.getElementById("personal_data_button").classList.remove("active");
    document.getElementById("personal").classList.remove("active");
    document.getElementById("films_button").classList.add("active");
    document.getElementById("films").classList.add("active");
    document.getElementById("personal_info").classList.add("hidden");
    document.getElementById("films_page").classList.remove("hidden");
});



document.getElementById("button_all").addEventListener("click", function(){
    event.preventDefault();
    if (count == 0){
        document.getElementById("unwrap").classList.add("hidden");
        document.getElementById("wrap").classList.remove("hidden");
        document.getElementById("wrap_liked").classList.remove("hidden");
        count = 1}
    else{
        document.getElementById("wrap").classList.add("hidden");
        document.getElementById("unwrap").classList.remove("hidden");
        document.getElementById("wrap_liked").classList.add("hidden");
        count = 0}
});
