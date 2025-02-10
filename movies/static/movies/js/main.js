// Переход шапки
window.addEventListener('scroll', trackscroll);
function trackscroll()
{
    let header = document.getElementById('header');
    if (window.pageYOffset > 0) {
        header.classList.add('top');
    }
    else {
        header.classList.remove('top');
    }
}


