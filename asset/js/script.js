// JavaScript для бургер-меню и навигации
document.addEventListener('DOMContentLoaded', function() {
    const burgerToggle = document.getElementById('burger-toggle');
    const menuItems = document.querySelectorAll('.menu-items a');
    
    // Закрытие меню при клике на ссылку (только на мобильных)
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                burgerToggle.checked = false;
            }
        });
    });
    
    // Закрытие меню при клике вне его области (только на мобильных)
    document.addEventListener('click', function(event) {
        if (window.innerWidth <= 768) {
            const isClickInsideMenu = event.target.closest('.nav-container');
            if (!isClickInsideMenu && burgerToggle.checked) {
                burgerToggle.checked = false;
            }
        }
    });
    
    // Сброс состояния меню при изменении размера окна
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            burgerToggle.checked = false;
        }
    });
    
    console.log('Сайт загружен! Адаптивное меню работает.');
});