// JavaScript для бургер-меню и навигации
document.addEventListener('DOMContentLoaded', function() {
    const burgerToggle = document.getElementById('burger-toggle');
    const menuItems = document.querySelectorAll('.menu-items a');
    
    // Закрытие меню при клике на ссылку
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            burgerToggle.checked = false;
        });
    });
    
    // Закрытие меню при клике вне его области
    document.addEventListener('click', function(event) {
        const isClickInsideMenu = event.target.closest('.nav-container');
        if (!isClickInsideMenu && burgerToggle.checked) {
            burgerToggle.checked = false;
        }
    });
    
    console.log('Сайт загружен! Используйте бургер-меню для навигации.');
});