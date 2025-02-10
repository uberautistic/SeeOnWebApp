$(document).ready(function() {
    $('#search-input').on('click', function(e) {
        //e.stopPropagation(); // Предотвращаем закрытие после клика на строку поиска
        //$('#header').toggleClass('full-screen'); // Добавляем/убираем класс full-screen
        e.stopPropagation();
        $('#header').addClass('full-screen');
        $('#search-container').addClass('open');
        $('#search-cancel').addClass('show');
        $('body').addClass('no-scroll');
        $('#search-container').empty();

        $('#profile_hidden').addClass('hidden');
        $('#toggle_neiro').removeClass('hidden');
    });

    // Закрываем заголовок при клике вне его
    $('#search-cancel').on('click', function() {
        $('#header').removeClass('full-screen');
        $('#search-container').removeClass('open');
        $('#search-cancel').removeClass('show');
        $('body').removeClass('no-scroll');
        $('#search-container').empty();
        $('#search-input').val('')
        $('#profile_hidden').removeClass('hidden');
        $('#toggle_neiro').addClass('hidden');
    });
});



