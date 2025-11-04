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
    <!-- Бургер меню -->
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
        <p>Используйте бургер-меню для навигации по сайту.</p>
    </main>

    <script src="asset/js/script.js"></script>
</body>
</html>""",

        "asset/css/style.css": """/* Стили для бургер-меню */
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
    position: relative;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    min-height: 60px;
}

.menu-items {
    display: none;
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    background: #333;
    padding: 1rem 0;
    list-style: none;
    z-index: 1;
}

.menu-items li {
    margin: 0;
}

.menu-items a {
    display: block;
    padding: 0.75rem 1.5rem;
    color: white;
    text-decoration: none;
    transition: background 0.3s;
}

.menu-items a:hover {
    background: #555;
}

/* Стили для бургер-кнопки */
.checkbox {
    position: absolute;
    display: none;
}

.hamburger-lines {
    display: block;
    height: 26px;
    width: 32px;
    position: absolute;
    top: 17px;
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

/* Анимация бургер-меню */
.checkbox:checked ~ .menu-items {
    display: block;
}

.checkbox:checked ~ .hamburger-lines .line1 {
    transform: rotate(45deg) translate(8px, 8px);
}

.checkbox:checked ~ .hamburger-lines .line2 {
    opacity: 0;
}

.checkbox:checked ~ .hamburger-lines .line3 {
    transform: rotate(-45deg) translate(8px, -8px);
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