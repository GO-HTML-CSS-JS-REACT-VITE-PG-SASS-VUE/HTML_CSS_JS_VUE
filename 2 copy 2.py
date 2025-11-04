import os

# Массив названий файлов
files = [
    "index.html",
    "asset/css/style.css",
    "asset/js/script.js",
    "about.html",
    "contact.html",
    "services.html",
    "portfolio.html"
]

# Функция для создания содержимого файлов
def get_file_content(filename):
    # Switch-case через словарь
    content_switcher = {
        "index.html": """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Главная страница</title>
    <link rel="stylesheet" href="asset/css/style.css">
</head>
<body>
    <!-- Адаптивное меню -->
    <nav class="navbar">
        <div class="nav-container">
            <input class="checkbox" type="checkbox" id="burger-toggle" />
            <label class="hamburger-lines" for="burger-toggle">
                <span class="line line1"></span>
                <span class="line line2"></span>
                <span class="line line3"></span>
            </label>
            
            <ul class="menu-items">
                <li><a href="index.html">Главная</a></li>
                <li><a href="about.html">О нас</a></li>
                <li><a href="services.html">Услуги</a></li>
                <li><a href="portfolio.html">Портфолио</a></li>
                <li><a href="contact.html">Контакты</a></li>
            </ul>
        </div>
    </nav>

    <main>
        <h1>Добро пожаловать на главную страницу!</h1>
        <p>На десктопе видно обычное меню, на мобильных - бургер-меню для навигации.</p>
    </main>

    <script src="asset/js/script.js"></script>
</body>
</html>""",

        "asset/css/style.css": """/* Стили для адаптивного меню */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

.navbar {
    background: #333;
    padding: 1rem 0;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
    position: relative;
}

/* Меню по умолчанию (для десктопа) */
.menu-items {
    display: flex;
    list-style: none;
    justify-content: center;
    gap: 2rem;
}

.menu-items li {
    margin: 0;
}

.menu-items a {
    display: block;
    padding: 0.5rem 1rem;
    color: white;
    text-decoration: none;
    transition: background 0.3s;
    border-radius: 4px;
}

.menu-items a:hover {
    background: #555;
}

/* Бургер-кнопка скрыта на десктопе */
.checkbox {
    display: none;
}

.hamburger-lines {
    display: none;
    height: 26px;
    width: 32px;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    left: 20px;
    z-index: 2;
    cursor: pointer;
}

.line {
    display: block;
    height: 4px;
    width: 100%;
    border-radius: 2px;
    background: white;
    margin-bottom: 5px;
    transition: transform 0.3s, opacity 0.3s;
}

.line:last-child {
    margin-bottom: 0;
}

/* Медиа-запросы для мобильных устройств */
@media (max-width: 768px) {
    /* Показываем бургер-кнопку */
    .hamburger-lines {
        display: block;
    }
    
    /* Скрываем меню по умолчанию */
    .menu-items {
        display: none;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        width: 100%;
        background: #333;
        padding: 1rem 0;
        gap: 0;
    }
    
    .menu-items li {
        width: 100%;
    }
    
    .menu-items a {
        padding: 0.75rem 1.5rem;
        border-radius: 0;
    }
    
    /* Показываем меню когда чекбокс активен */
    .checkbox:checked ~ .menu-items {
        display: flex;
    }
    
    /* Анимация бургер-кнопки */
    .checkbox:checked ~ .hamburger-lines .line1 {
        transform: rotate(45deg) translate(8px, 8px);
    }
    
    .checkbox:checked ~ .hamburger-lines .line2 {
        opacity: 0;
    }
    
    .checkbox:checked ~ .hamburger-lines .line3 {
        transform: rotate(-45deg) translate(8px, -8px);
    }
}

/* Основной контент */
main {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
}

h1 {
    color: #333;
    margin-bottom: 1rem;
}

p {
    color: #666;
    line-height: 1.8;
}""",

        "asset/js/script.js": """// JavaScript для бургер-меню и навигации
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
});""",

        "about.html": """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>О нас</title>
    <link rel="stylesheet" href="asset/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <input class="checkbox" type="checkbox" id="burger-toggle" />
            <label class="hamburger-lines" for="burger-toggle">
                <span class="line line1"></span>
                <span class="line line2"></span>
                <span class="line line3"></span>
            </label>
            
            <ul class="menu-items">
                <li><a href="index.html">Главная</a></li>
                <li><a href="about.html">О нас</a></li>
                <li><a href="services.html">Услуги</a></li>
                <li><a href="portfolio.html">Портфолио</a></li>
                <li><a href="contact.html">Контакты</a></li>
            </ul>
        </div>
    </nav>

    <main>
        <h1>О нашей компании</h1>
        <p>Мы занимаемся созданием качественных веб-сайтов с современным дизайном.</p>
    </main>

    <script src="asset/js/script.js"></script>
</body>
</html>""",

        "contact.html": """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Контакты</title>
    <link rel="stylesheet" href="asset/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <input class="checkbox" type="checkbox" id="burger-toggle" />
            <label class="hamburger-lines" for="burger-toggle">
                <span class="line line1"></span>
                <span class="line line2"></span>
                <span class="line line3"></span>
            </label>
            
            <ul class="menu-items">
                <li><a href="index.html">Главная</a></li>
                <li><a href="about.html">О нас</a></li>
                <li><a href="services.html">Услуги</a></li>
                <li><a href="portfolio.html">Портфолио</a></li>
                <li><a href="contact.html">Контакты</a></li>
            </ul>
        </div>
    </nav>

    <main>
        <h1>Наши контакты</h1>
        <p>Свяжитесь с нами для обсуждения вашего проекта.</p>
    </main>

    <script src="asset/js/script.js"></script>
</body>
</html>""",

        "services.html": """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Услуги</title>
    <link rel="stylesheet" href="asset/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <input class="checkbox" type="checkbox" id="burger-toggle" />
            <label class="hamburger-lines" for="burger-toggle">
                <span class="line line1"></span>
                <span class="line line2"></span>
                <span class="line line3"></span>
            </label>
            
            <ul class="menu-items">
                <li><a href="index.html">Главная</a></li>
                <li><a href="about.html">О нас</a></li>
                <li><a href="services.html">Услуги</a></li>
                <li><a href="portfolio.html">Портфолио</a></li>
                <li><a href="contact.html">Контакты</a></li>
            </ul>
        </div>
    </nav>

    <main>
        <h1>Наши услуги</h1>
        <p>Мы предлагаем полный цикл разработки веб-сайтов.</p>
    </main>

    <script src="asset/js/script.js"></script>
</body>
</html>""",

        "portfolio.html": """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Портфолио</title>
    <link rel="stylesheet" href="asset/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <input class="checkbox" type="checkbox" id="burger-toggle" />
            <label class="hamburger-lines" for="burger-toggle">
                <span class="line line1"></span>
                <span class="line line2"></span>
                <span class="line line3"></span>
            </label>
            
            <ul class="menu-items">
                <li><a href="index.html">Главная</a></li>
                <li><a href="about.html">О нас</a></li>
                <li><a href="services.html">Услуги</a></li>
                <li><a href="portfolio.html">Портфолио</a></li>
                <li><a href="contact.html">Контакты</a></li>
            </ul>
        </div>
    </nav>

    <main>
        <h1>Наше портфолио</h1>
        <p>Посмотрите примеры наших работ.</p>
    </main>

    <script src="asset/js/script.js"></script>
</body>
</html>"""
    }
    
    # Возвращаем содержимое или пустую строку если файл не найден
    return content_switcher.get(filename, "")

# Создание файлов
for file_path in files:
    # Создаем директории если нужно (только для файлов с путями)
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    # Получаем содержимое файла
    content = get_file_content(file_path)
    
    # Создаем файл
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Создан файл: {file_path}")

print("Все файлы успешно созданы!")