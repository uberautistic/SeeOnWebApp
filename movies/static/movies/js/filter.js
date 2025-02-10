    document.getElementById("sort-content").classList.add("hidden");
    document.getElementById("parameters_filtration").classList.add("hidden");
    document.getElementById("search_settings").classList.add("hidden");
    count = 0;
    counterpoint = 0;
    counterpoint2 = 0;
    counterpoint3 = 0;
    counterpoint4 = 0;
    counterpoint5=0;
    counterpoint6=0;
    counterpoint7=0;
    counterpoint8=0;
    document.getElementById("genre").classList.remove("active");
    document.getElementById("country").classList.remove("active");
    document.getElementById("year").classList.remove("active");
    document.getElementById("age").classList.remove("active");


document.getElementById("filter").addEventListener("click", function(event){
    event.preventDefault();
    if (count == 0){
        document.getElementById("parameters_selection").classList.add("hidden");
        document.getElementById("parameters_filtration").classList.remove("hidden");
        document.getElementById("sort-content").classList.add("hidden");
        document.getElementById("search_settings").classList.remove("hidden");
        count = 1;
    }
    else{
        document.getElementById("filter").classList.remove("hidden");
        document.getElementById("parameters_selection").classList.remove("hidden");
        document.getElementById("sort-content").classList.add("hidden");
        document.getElementById("parameters_filtration").classList.add("hidden");
        document.getElementById("search_settings").classList.add("hidden");
        count = 0;
    }
});

document.getElementById("parameters_selection").addEventListener("click", function(event){
    event.preventDefault();
    if (count == 0){
        document.getElementById("filter").classList.add("hidden");
        document.getElementById("parameters_filtration").classList.add("hidden");
        document.getElementById("sort-content").classList.remove("hidden");
        document.getElementById("search_settings").classList.remove("hidden");
        count = 1;
    }
    else{
        document.getElementById("filter").classList.remove("hidden");
        document.getElementById("parameters_selection").classList.remove("hidden");
        document.getElementById("sort-content").classList.add("hidden");
        document.getElementById("parameters_filtration").classList.add("hidden");
        document.getElementById("search_settings").classList.add("hidden");
        count = 0;
    }
});

document.getElementById("reset_settings").addEventListener("click", function(){
        document.getElementById("filter").classList.remove("hidden");
        document.getElementById("parameters_selection").classList.remove("hidden");
        document.getElementById("sort-content").classList.add("hidden");
        document.getElementById("parameters_filtration").classList.add("hidden");

        document.getElementById("genre").classList.remove("active");
        document.getElementById("country").classList.remove("active");
        document.getElementById("year").classList.remove("active");
        document.getElementById("age").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        count = 0;
});

document.getElementById("genre_button").addEventListener("click", function(event){
    event.preventDefault();
     if (counterpoint == 0){
        document.getElementById("genre_div").classList.add("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint = 1;
        }
     else{
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint = 0;
        }
});

document.getElementById("genre_button").addEventListener("click", function(){
     if (counterpoint2 == 0){
        document.getElementById("genre_div").classList.add("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint2 = 1;
        }
     else{
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint2 = 0;
        }
});

document.getElementById("country_button").addEventListener("click", function(event){
    event.preventDefault();
     if (counterpoint3 == 0){
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.add("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint3 = 1;
        }
     else{
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint3 = 0;
        }
});

document.getElementById("age_button").addEventListener("click", function(event){
     event.preventDefault();
     if (counterpoint4 == 0){
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.add("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint4 = 1;
        }
     else{
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint4 = 0;
        }
});





document.getElementById("year_button").addEventListener("click", function(event){
     event.preventDefault();
     if (counterpoint5 == 0){
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.add("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint5 = 1;
        }
     else{
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint5 = 0;
        }
});

document.getElementById("date_premier_button").addEventListener("click", function(event){
    event.preventDefault();
    if (counterpoint6==0){
        document.getElementById("date_sort_div").classList.add("active");
        document.getElementById("rate_sort_div").classList.remove("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint6=1;
    }
    else{
        document.getElementById("date_sort_div").classList.remove("active");
        document.getElementById("rate_sort_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint6=0;
    }
});

document.getElementById("rating_button").addEventListener("click", function(event){
    event.preventDefault();
    if (counterpoint7==0){
        document.getElementById("date_sort_div").classList.remove("active");
        document.getElementById("rate_sort_div").classList.add("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint7=1;
    }
    else{
        document.getElementById("date_sort_div").classList.remove("active");
        document.getElementById("rate_sort_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint7=0;
    }
});

document.getElementById("type_button").addEventListener("click", function(event){
    event.preventDefault();
     if (counterpoint8 == 0){
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.add("active");
        document.getElementById("search_settings").classList.remove("hidden");
        counterpoint8 = 1;
        }
     else{
        document.getElementById("genre_div").classList.remove("active");
        document.getElementById("country_div").classList.remove("active");
        document.getElementById("age_div").classList.remove("active");
        document.getElementById("year_div").classList.remove("active");
        document.getElementById("type_div").classList.remove("active");
        document.getElementById("search_settings").classList.add("hidden");
        counterpoint8 = 0;
        }
});

