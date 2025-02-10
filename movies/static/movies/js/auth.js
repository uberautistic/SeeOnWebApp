/* Authentication */

document.getElementById("login_button").addEventListener("click", function(){
    document.getElementById("modal").classList.add("open");
    document.getElementById("modal_mail_auth").classList.add("open");
});

document.getElementById("cancel_modal_auth").addEventListener("click", function(){
    document.getElementById("modal_mail_auth").classList.remove("open");
    document.getElementById("modal_shadow_auth").classList.remove("open");

});
document.getElementById("continue_button_auth").addEventListener("click", function(){
    document.getElementById("modal_mail_auth").classList.remove("open");
    document.getElementById("modal_pass_auth").classList.add("open");

});

document.getElementById("back_pass_auth").addEventListener("click", function(){
    document.getElementById("modal_pass_auth").classList.remove("open");
    document.getElementById("modal_mail_auth").classList.add("open");

});

document.getElementById("cancel_modal_pass_auth").addEventListener("click", function(){
    document.getElementById("modal_pass_auth").classList.remove("open");
    document.getElementById("modal_shadow_auth").classList.remove("open");

});


/* Authentication TO Registration */

document.getElementById("register_button_mail").addEventListener("click", function(){
    document.getElementById("modal_mail_auth").classList.remove("open");
    document.getElementById("modal_mail_first").classList.add("open");

});

document.getElementById("register_button_pass").addEventListener("click", function(){
    document.getElementById("modal_pass_auth").classList.remove("open");
    document.getElementById("modal_mail_first").classList.add("open");

});

/* Authentication */

document.getElementById("continue_button").addEventListener("click", function(){
    document.getElementById("modal_mail_first").classList.remove("open");
    document.getElementById("modal_name").classList.add("open");
});

document.getElementById("cancel_modal_pass").addEventListener("click", function(){
    document.getElementById("modal_shadow_auth").classList.remove("open");
    document.getElementById("modal_pass").classList.remove("open");
});

document.getElementById("back_pass").addEventListener("click", function(){
    document.getElementById("modal_pass").classList.remove("open");
    document.getElementById("modal_name").classList.add("open");

});

document.getElementById("done_button").addEventListener("click", function(){
    document.getElementById("modal_pass").classList.remove("open");
    document.getElementById("modal_name").classList.add("open");

});



document.getElementById("cancel_modal").addEventListener("click", function(){
    document.getElementById("modal_mail_first").classList.remove("open");
    document.getElementById("modal_shadow_auth").classList.remove("open");

});
document.getElementById("continue_button_name").addEventListener("click", function(){
    document.getElementById("modal_name").classList.remove("open");
    document.getElementById("modal_pass").classList.add("open");

});

document.getElementById("back_name").addEventListener("click", function(){
    document.getElementById("modal_name").classList.remove("open");
    document.getElementById("modal_mail_first").classList.add("open");

});

document.getElementById("cancel_modal_name").addEventListener("click", function(){
    document.getElementById("modal_name").classList.remove("open");
    document.getElementById("modal_shadow_auth").classList.remove("open");

});

document.getElementById("continue_button").addEventListener("click", function(){
    document.getElementById("modal_mail_first").classList.remove("open");
    document.getElementById("modal_name").classList.add("open");
});

document.getElementById("cancel_modal_pass").addEventListener("click", function(){
    document.getElementById("modal_shadow_auth").classList.remove("open");
    document.getElementById("modal_pass").classList.remove("open");
});

document.getElementById("back_pass").addEventListener("click", function(){
    document.getElementById("modal_pass").classList.remove("open");
    document.getElementById("modal_name").classList.add("open");

});

document.getElementById("done_button").addEventListener("click", function(){
    document.getElementById("modal_pass").classList.remove("open");
    document.getElementById("modal_name").classList.add("open");

});