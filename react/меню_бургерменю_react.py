import os
import json

# Структура файлов для React проекта
files = {
    "package.json": {
        "content": {
            "name": "burger-menu-app",
            "version": "1.0.0",
            "type": "module",
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0"
            },
            "devDependencies": {
                "@types/react": "^18.2.0",
                "@types/react-dom": "^18.2.0",
                "@vitejs/plugin-react": "^4.0.0",
                "vite": "^4.4.0"
            }
        },
        "is_json": True
    },
    
    "vite.config.js": {
        "content": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  }
})""",
        "is_json": False
    },
    
    "index.html": {
        "content": """<!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React Burger Menu App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>""",
        "is_json": False
    },
    
    "src/main.jsx": {
        "content": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""",
        "is_json": False
    },
    
    "src/index.css": {
        "content": """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  background-color: #f5f5f5;
}

#root {
  min-height: 100vh;
}""",
        "is_json": False
    },
    
    "src/App.jsx": {
        "content": """import React, { useState } from 'react'
import BurgerMenu from './components/BurgerMenu'
import Home from './pages/Home'
import About from './pages/About'
import Services from './pages/Services'
import Portfolio from './pages/Portfolio'
import Contact from './pages/Contact'
import './App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('home')

  const renderPage = () => {
    switch(currentPage) {
      case 'home':
        return <Home />
      case 'about':
        return <About />
      case 'services':
        return <Services />
      case 'portfolio':
        return <Portfolio />
      case 'contact':
        return <Contact />
      default:
        return <Home />
    }
  }

  return (
    <div className="App">
      <BurgerMenu currentPage={currentPage} onPageChange={setCurrentPage} />
      <main className="main-content">
        {renderPage()}
      </main>
    </div>
  )
}

export default App""",
        "is_json": False
    },
    
    "src/App.css": {
        "content": """.App {
  min-height: 100vh;
}

.main-content {
  padding-top: 70px;
  min-height: calc(100vh - 70px);
}

.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.page h1 {
  color: #333;
  margin-bottom: 1rem;
  font-size: 2.5rem;
}

.page p {
  color: #666;
  font-size: 1.1rem;
  line-height: 1.8;
}

.page-content {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}""",
        "is_json": False
    },
    
    "src/components/BurgerMenu.jsx": {
        "content": """import React, { useState } from 'react'
import './BurgerMenu.css'

const BurgerMenu = ({ currentPage, onPageChange }) => {
  const [isOpen, setIsOpen] = useState(false)

  const menuItems = [
    { key: 'home', label: 'Главная' },
    { key: 'about', label: 'О нас' },
    { key: 'services', label: 'Услуги' },
    { key: 'portfolio', label: 'Портфолио' },
    { key: 'contact', label: 'Контакты' }
  ]

  const handleMenuToggle = () => {
    setIsOpen(!isOpen)
  }

  const handleMenuItemClick = (pageKey) => {
    onPageChange(pageKey)
    setIsOpen(false)
  }

  return (
    <nav className="navbar">
      <div className="nav-container">
        <div className="logo">
          React App
        </div>
        
        <div className={`burger-menu ${isOpen ? 'open' : ''}`} onClick={handleMenuToggle}>
          <span className="burger-line"></span>
          <span className="burger-line"></span>
          <span className="burger-line"></span>
        </div>
        
        <ul className={`menu-items ${isOpen ? 'open' : ''}`}>
          {menuItems.map(item => (
            <li key={item.key} className="menu-item">
              <button 
                className={`menu-link ${currentPage === item.key ? 'active' : ''}`}
                onClick={() => handleMenuItemClick(item.key)}
              >
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  )
}

export default BurgerMenu""",
        "is_json": False
    },
    
    "src/components/BurgerMenu.css": {
        "content": """.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: #2c3e50;
  padding: 1rem 0;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  z-index: 1000;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
}

.logo {
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
}

.burger-menu {
  display: none;
  flex-direction: column;
  cursor: pointer;
  padding: 5px;
}

.burger-line {
  width: 25px;
  height: 3px;
  background: white;
  margin: 3px 0;
  transition: 0.3s;
}

.menu-items {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.menu-item {
  margin: 0;
}

.menu-link {
  background: none;
  border: none;
  color: white;
  text-decoration: none;
  font-size: 1rem;
  cursor: pointer;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  transition: background 0.3s;
  font-family: inherit;
}

.menu-link:hover {
  background: #34495e;
}

.menu-link.active {
  background: #3498db;
}

/* Мобильные стили */
@media (max-width: 768px) {
  .burger-menu {
    display: flex;
  }

  .menu-items {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #2c3e50;
    flex-direction: column;
    gap: 0;
    transform: translateY(-100%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
  }

  .menu-items.open {
    transform: translateY(0);
    opacity: 1;
    visibility: visible;
  }

  .menu-item {
    width: 100%;
  }

  .menu-link {
    display: block;
    width: 100%;
    text-align: left;
    padding: 1rem 2rem;
    border-radius: 0;
    border-bottom: 1px solid #34495e;
  }

  /* Анимация бургера */
  .burger-menu.open .burger-line:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }

  .burger-menu.open .burger-line:nth-child(2) {
    opacity: 0;
  }

  .burger-menu.open .burger-line:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -6px);
  }
}""",
        "is_json": False
    },
    
    "src/pages/Home.jsx": {
        "content": """import React from 'react'

const Home = () => {
  return (
    <div className="page">
      <div className="page-content">
        <h1>Добро пожаловать!</h1>
        <p>
          Это главная страница нашего React приложения с бургер-меню.
          Используйте меню для навигации между разделами сайта.
        </p>
        <p>
          Приложение полностью адаптивно и отлично работает как на десктопе, 
          так и на мобильных устройствах.
        </p>
      </div>
    </div>
  )
}

export default Home""",
        "is_json": False
    },
    
    "src/pages/About.jsx": {
        "content": """import React from 'react'

const About = () => {
  return (
    <div className="page">
      <div className="page-content">
        <h1>О нас</h1>
        <p>
          Мы команда профессионалов, занимающихся разработкой современных 
          веб-приложений на React. Наш опыт позволяет создавать качественные 
          и производительные решения.
        </p>
        <p>
          Мы используем современные технологии и лучшие практики разработки 
          для достижения outstanding результатов.
        </p>
      </div>
    </div>
  )
}

export default About""",
        "is_json": False
    },
    
    "src/pages/Services.jsx": {
        "content": """import React from 'react'

const Services = () => {
  return (
    <div className="page">
      <div className="page-content">
        <h1>Наши услуги</h1>
        <p>
          Мы предлагаем полный цикл разработки веб-приложений:
        </p>
        <ul style={{marginLeft: '2rem', marginTop: '1rem'}}>
          <li>Разработка на React</li>
          <li>Создание адаптивных интерфейсов</li>
          <li>Оптимизация производительности</li>
          <li>Тестирование и деплой</li>
        </ul>
      </div>
    </div>
  )
}

export default Services""",
        "is_json": False
    },
    
    "src/pages/Portfolio.jsx": {
        "content": """import React from 'react'

const Portfolio = () => {
  return (
    <div className="page">
      <div className="page-content">
        <h1>Портфолио</h1>
        <p>
          Вот некоторые из наших последних проектов:
        </p>
        <div style={{display: 'grid', gap: '1rem', marginTop: '1.5rem'}}>
          <div style={{padding: '1rem', background: '#f8f9fa', borderRadius: '5px'}}>
            <strong>Корпоративный портал</strong> - React, Redux, TypeScript
          </div>
          <div style={{padding: '1rem', background: '#f8f9fa', borderRadius: '5px'}}>
            <strong>Интернет-магазин</strong> - Next.js, Stripe, MongoDB
          </div>
          <div style={{padding: '1rem', background: '#f8f9fa', borderRadius: '5px'}}>
            <strong>Панель управления</strong> - React, D3.js, WebSocket
          </div>
        </div>
      </div>
    </div>
  )
}

export default Portfolio""",
        "is_json": False
    },
    
    "src/pages/Contact.jsx": {
        "content": """import React from 'react'

const Contact = () => {
  return (
    <div className="page">
      <div className="page-content">
        <h1>Контакты</h1>
        <p>
          Свяжитесь с нами для обсуждения вашего проекта:
        </p>
        <div style={{marginTop: '1.5rem'}}>
          <p><strong>Email:</strong> hello@example.com</p>
          <p><strong>Телефон:</strong> +7 (999) 123-45-67</p>
          <p><strong>Адрес:</strong> г. Москва, ул. Примерная, д. 123</p>
        </div>
      </div>
    </div>
  )
}

export default Contact""",
        "is_json": False
    }
}

# Создание файлов
for file_path, file_info in files.items():
    # Создаем директории если нужно
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    # Получаем содержимое файла
    if file_info["is_json"]:
        content = json.dumps(file_info["content"], indent=2, ensure_ascii=False)
    else:
        content = file_info["content"]
    
    # Создаем файл
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Создан файл: {file_path}")

print("\\nReact проект успешно создан!")
print("\\nДля запуска проекта выполните команды:")
print("npm install")
print("npm run dev")