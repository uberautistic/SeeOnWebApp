count = 0;
$(document).ready(function()
 {
    $('#neiro_but').on('click', function(e)
    {
        //e.stopPropagation(); // Предотвращаем закрытие после клика на строку поиска
        //$('#header').toggleClass('full-screen'); // Добавляем/убираем класс full-screen
        e.stopPropagation();
        if (count == 0){
        $('#profile_text').addClass('active');
        $('#theme_content-item').addClass('active');
        $('#toggle_neiro').setAttribute("data-search-mode",1);
        count = 1;
        }
        else{
        $('#profile_text').removeClass('active');
        $('#theme_content-item').removeClass('active');
        $('#toggle_neiro').setAttribute("data-search-mode",0);
        count = 0;
        }
        })});