import os
import json

# Структура файлов для React проекта с Vite
files = {
    "package.json": {
        "content": {
            "name": "react-burger-menu-app",
            "private": True,
            "version": "1.0.0",
            "type": "module",
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview",
                "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0"
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0"
            },
            "devDependencies": {
                "@types/react": "^18.2.0",
                "@types/react-dom": "^18.2.0",
                "@vitejs/plugin-react": "^4.0.0",
                "eslint": "^8.45.0",
                "eslint-plugin-react": "^7.32.2",
                "eslint-plugin-react-hooks": "^4.6.0",
                "eslint-plugin-react-refresh": "^0.4.3",
                "vite": "^4.4.0"
            }
        },
        "is_json": True
    },
    
    "vite.config.js": {
        "content": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
})""",
        "is_json": False
    },
    
    "index.html": {
        "content": """<!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
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
    
    ".gitignore": {
        "content": """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?""",
        "is_json": False
    },
    
    "public/vite.svg": {
        "content": """<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="iconify iconify--logos" width="31.88" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 256 257"><defs><linearGradient id="IconifyId1813088fe1fbc01fb466" x1="-.828%" x2="57.636%" y1="7.652%" y2="78.411%"><stop offset="0%" stop-color="#41D1FF"></stop><stop offset="100%" stop-color="#BD34FE"></stop></linearGradient><linearGradient id="IconifyId1813088fe1fbc01fb467" x1="43.376%" x2="50.316%" y1="2.242%" y2="89.03%"><stop offset="0%" stop-color="#FFEA83"></stop><stop offset="8.333%" stop-color="#FFDD35"></stop><stop offset="100%" stop-color="#FFA800"></stop></linearGradient></defs><path fill="url(#IconifyId1813088fe1fbc01fb466)" d="M255.153 37.938L134.897 252.976c-2.483 4.44-8.862 4.466-11.382.048L.875 37.958c-2.746-4.814 1.371-10.646 6.827-9.67l120.385 21.517a6.537 6.537 0 0 0 2.322-.004l117.867-21.483c5.438-.991 9.574 4.796 6.877 9.62Z"></path><path fill="url(#IconifyId1813088fe1fbc01fb467)" d="M185.432.063L96.44 17.501a3.268 3.268 0 0 0-2.634 3.014l-5.474 92.456a3.268 3.268 0 0 0 3.997 3.378l24.777-5.718c2.318-.535 4.413 1.507 3.936 3.838l-7.361 36.047c-.495 2.426 1.782 4.5 4.151 3.78l15.304-4.649c2.372-.72 4.652 1.36 4.15 3.788l-11.698 56.621c-.732 3.542 3.979 5.473 5.943 2.437l1.313-2.028l72.516-144.72c1.215-2.423-.88-5.186-3.54-4.672l-25.505 4.922c-2.396.462-4.435-1.77-3.759-4.114l16.646-57.705c.677-2.35-1.37-4.583-3.769-4.113Z"></path></svg>""",
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
        "content": """/* Reset and base styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --primary-color: #2c3e50;
  --secondary-color: #3498db;
  --accent-color: #e74c3c;
  --text-light: #ecf0f1;
  --text-dark: #2c3e50;
  --bg-light: #f8f9fa;
  --shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  --border-radius: 8px;
  --transition: all 0.3s ease;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--text-dark);
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

#root {
  min-height: 100vh;
}

/* Scrollbar styles */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: var(--secondary-color);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #2980b9;
}""",
        "is_json": False
    },
    
    "src/App.jsx": {
        "content": """import React, { useState, useEffect } from 'react'
import BurgerMenu from './components/BurgerMenu'
import Home from './pages/Home'
import About from './pages/About'
import Services from './pages/Services'
import Portfolio from './pages/Portfolio'
import Contact from './pages/Contact'
import './App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('home')
  const [isLoading, setIsLoading] = useState(true)

  // Simulate loading
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false)
    }, 1000)
    return () => clearTimeout(timer)
  }, [])

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

  if (isLoading) {
    return (
      <div className="loading-screen">
        <div className="loading-spinner"></div>
        <h2>Загрузка...</h2>
      </div>
    )
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
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding-top: 80px;
}

/* Loading screen */
.loading-screen {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Page transitions */
.page-enter {
  opacity: 0;
  transform: translateY(20px);
}

.page-enter-active {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 300ms, transform 300ms;
}

/* Responsive design */
@media (max-width: 768px) {
  .main-content {
    padding-top: 70px;
  }
}""",
        "is_json": False
    },
    
    "src/components/BurgerMenu.jsx": {
        "content": """import React, { useState, useEffect } from 'react'
import './BurgerMenu.css'

const BurgerMenu = ({ currentPage, onPageChange }) => {
  const [isOpen, setIsOpen] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)

  const menuItems = [
    { key: 'home', label: 'Главная', icon: '🏠' },
    { key: 'about', label: 'О нас', icon: '👥' },
    { key: 'services', label: 'Услуги', icon: '⚙️' },
    { key: 'portfolio', label: 'Портфолио', icon: '💼' },
    { key: 'contact', label: 'Контакты', icon: '📞' }
  ]

  // Handle scroll effect
  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const handleMenuToggle = () => {
    setIsOpen(!isOpen)
  }

  const handleMenuItemClick = (pageKey) => {
    onPageChange(pageKey)
    setIsOpen(false)
  }

  // Close menu on escape key
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape' && isOpen) {
        setIsOpen(false)
      }
    }
    document.addEventListener('keydown', handleEscape)
    return () => document.removeEventListener('keydown', handleEscape)
  }, [isOpen])

  return (
    <nav className={`navbar ${isScrolled ? 'scrolled' : ''}`}>
      <div className="nav-container">
        <div className="logo">
          <span className="logo-icon">⚡</span>
          Vite React
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
                <span className="menu-icon">{item.icon}</span>
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
  background: rgba(44, 62, 80, 0.95);
  backdrop-filter: blur(10px);
  padding: 1rem 0;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  transition: var(--transition);
}

.navbar.scrolled {
  background: rgba(44, 62, 80, 0.98);
  padding: 0.75rem 0;
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
  color: var(--text-light);
  font-size: 1.5rem;
  font-weight: bold;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo-icon {
  font-size: 1.8rem;
}

.burger-menu {
  display: none;
  flex-direction: column;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: none;
  z-index: 1001;
}

.burger-line {
  width: 25px;
  height: 3px;
  background: var(--text-light);
  margin: 3px 0;
  transition: var(--transition);
  border-radius: 2px;
}

.menu-items {
  display: flex;
  list-style: none;
  gap: 1.5rem;
  margin: 0;
  padding: 0;
  align-items: center;
}

.menu-item {
  margin: 0;
}

.menu-link {
  background: none;
  border: none;
  color: var(--text-light);
  text-decoration: none;
  font-size: 1rem;
  cursor: pointer;
  padding: 0.75rem 1.5rem;
  border-radius: var(--border-radius);
  transition: var(--transition);
  font-family: inherit;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  position: relative;
  overflow: hidden;
}

.menu-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.5s;
}

.menu-link:hover::before {
  left: 100%;
}

.menu-link:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

.menu-link.active {
  background: var(--secondary-color);
  box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
}

.menu-icon {
  font-size: 1.1rem;
}

/* Мобильные стили */
@media (max-width: 768px) {
  .nav-container {
    padding: 0 1rem;
  }

  .burger-menu {
    display: flex;
  }

  .menu-items {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(44, 62, 80, 0.98);
    backdrop-filter: blur(10px);
    flex-direction: column;
    justify-content: center;
    gap: 0;
    transform: translateX(-100%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .menu-items.open {
    transform: translateX(0);
    opacity: 1;
    visibility: visible;
  }

  .menu-item {
    width: 100%;
    text-align: center;
  }

  .menu-link {
    display: flex;
    justify-content: center;
    width: 100%;
    text-align: center;
    padding: 1.5rem 2rem;
    border-radius: 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    font-size: 1.2rem;
  }

  .menu-link:last-child {
    border-bottom: none;
  }

  /* Анимация бургера */
  .burger-menu.open .burger-line:nth-child(1) {
    transform: rotate(45deg) translate(6px, 6px);
  }

  .burger-menu.open .burger-line:nth-child(2) {
    opacity: 0;
    transform: translateX(-10px);
  }

  .burger-menu.open .burger-line:nth-child(3) {
    transform: rotate(-45deg) translate(6px, -6px);
  }

  .logo {
    font-size: 1.3rem;
  }
}

/* Анимация для пунктов меню при открытии */
.menu-items.open .menu-item {
  animation: slideIn 0.4s ease-out forwards;
}

.menu-items.open .menu-item:nth-child(1) { animation-delay: 0.1s; }
.menu-items.open .menu-item:nth-child(2) { animation-delay: 0.2s; }
.menu-items.open .menu-item:nth-child(3) { animation-delay: 0.3s; }
.menu-items.open .menu-item:nth-child(4) { animation-delay: 0.4s; }
.menu-items.open .menu-item:nth-child(5) { animation-delay: 0.5s; }

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
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
        <h1>🚀 Добро пожаловать в Vite React App!</h1>
        <p>
          Это современное React приложение собрано с использованием <strong>Vite</strong> - 
          быстрого сборщика для веб-приложений.
        </p>
        <div className="features-grid">
          <div className="feature-card">
            <h3>⚡ Молниеносная сборка</h3>
            <p>Vite обеспечивает невероятно быструю разработку с мгновенной перезагрузкой</p>
          </div>
          <div className="feature-card">
            <h3>🎯 Современный стек</h3>
            <p>React 18, Hooks, современный JavaScript и CSS</p>
          </div>
          <div className="feature-card">
            <h3>📱 Адаптивный дизайн</h3>
            <p>Идеально работает на всех устройствах с бургер-меню</p>
          </div>
        </div>
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
        <h1>👥 О нашем проекте</h1>
        <p>
          Этот проект демонстрирует возможности современной веб-разработки 
          с использованием React и Vite.
        </p>
        
        <div className="tech-stack">
          <h2>🛠 Технологический стек</h2>
          <ul>
            <li><strong>Vite</strong> - сборщик проекта</li>
            <li><strong>React 18</strong> - пользовательский интерфейс</li>
            <li><strong>CSS3</strong> - стили и анимации</li>
            <li><strong>ES6+</strong> - современный JavaScript</li>
          </ul>
        </div>
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
  const services = [
    {
      title: "React Разработка",
      description: "Создание современных SPA приложений",
      features: ["Хуки и Context API", "Роутинг", "Оптимизация"]
    },
    {
      title: "Vite Сборка",
      description: "Быстрая разработка и сборка",
      features: ["HMR", "Tree Shaking", "Оптимизация"]
    },
    {
      title: "UI/UX Дизайн",
      description: "Современные интерфейсы",
      features: ["Адаптивность", "Анимации", "Доступность"]
    }
  ]

  return (
    <div className="page">
      <div className="page-content">
        <h1>⚙️ Наши услуги</h1>
        <p>Мы предлагаем полный цикл разработки современных веб-приложений</p>
        
        <div className="services-grid">
          {services.map((service, index) => (
            <div key={index} className="service-card">
              <h3>{service.title}</h3>
              <p>{service.description}</p>
              <ul>
                {service.features.map((feature, idx) => (
                  <li key={idx}>{feature}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
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
  const projects = [
    {
      title: "Корпоративный портал",
      tech: ["React", "Vite", "CSS3"],
      description: "Панель управления с аналитикой"
    },
    {
      title: "Интернет-магазин",
      tech: ["React", "Context API", "Vite"],
      description: "E-commerce решение с корзиной"
    },
    {
      title: "Дашборд аналитики",
      tech: ["React", "Charts", "Vite"],
      description: "Визуализация данных в реальном времени"
    }
  ]

  return (
    <div className="page">
      <div className="page-content">
        <h1>💼 Наше портфолио</h1>
        <p>Примеры наших последних проектов, созданных с использованием React и Vite</p>
        
        <div className="portfolio-grid">
          {projects.map((project, index) => (
            <div key={index} className="project-card">
              <h3>{project.title}</h3>
              <p>{project.description}</p>
              <div className="tech-tags">
                {project.tech.map((tech, idx) => (
                  <span key={idx} className="tech-tag">{tech}</span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Portfolio""",
        "is_json": False
    },
    
    "src/pages/Contact.jsx": {
        "content": """import React, { useState } from 'react'

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  })

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    alert('Сообщение отправлено! (Это демо)')
    setFormData({ name: '', email: '', message: '' })
  }

  return (
    <div className="page">
      <div className="page-content">
        <h1>📞 Свяжитесь с нами</h1>
        
        <div className="contact-grid">
          <div className="contact-info">
            <h2>Контактная информация</h2>
            <div className="contact-item">
              <strong>📧 Email:</strong> hello@vite-react-app.com
            </div>
            <div className="contact-item">
              <strong>📱 Телефон:</strong> +7 (999) 123-45-67
            </div>
            <div className="contact-item">
              <strong>🏢 Адрес:</strong> г. Москва, ул. Технологическая, д. 42
            </div>
          </div>
          
          <form className="contact-form" onSubmit={handleSubmit}>
            <h2>Форма обратной связи</h2>
            
            <div className="form-group">
              <label htmlFor="name">Имя:</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="email">Email:</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="message">Сообщение:</label>
              <textarea
                id="message"
                name="message"
                rows="5"
                value={formData.message}
                onChange={handleChange}
                required
              ></textarea>
            </div>
            
            <button type="submit" className="submit-btn">
              Отправить сообщение
            </button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default Contact""",
        "is_json": False
    },
    
    "src/styles/global.css": {
        "content": """/* Global styles for pages */
.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.page-content {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.page h1 {
  color: var(--text-dark);
  margin-bottom: 1.5rem;
  font-size: 2.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page p {
  color: var(--text-dark);
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

/* Features grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.feature-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  border-radius: 15px;
  text-align: center;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-card h3 {
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

/* Services grid */
.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.service-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: var(--shadow);
  border-left: 4px solid var(--secondary-color);
  transition: var(--transition);
}

.service-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.service-card h3 {
  color: var(--text-dark);
  margin-bottom: 1rem;
}

.service-card ul {
  margin-top: 1rem;
  padding-left: 1.5rem;
}

.service-card li {
  margin-bottom: 0.5rem;
  color: #666;
}

/* Portfolio grid */
.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.project-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: var(--shadow);
  transition: var(--transition);
  border: 1px solid #e9ecef;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.tech-tag {
  background: var(--secondary-color);
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

/* Contact styles */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-top: 2rem;
}

.contact-info {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: var(--shadow);
}

.contact-item {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: var(--bg-light);
  border-radius: 8px;
}

.contact-form {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: var(--shadow);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-dark);
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  transition: var(--transition);
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--secondary-color);
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.submit-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  width: 100%;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

/* Tech stack */
.tech-stack {
  margin-top: 2rem;
  padding: 1.5rem;
  background: var(--bg-light);
  border-radius: 10px;
}

.tech-stack h2 {
  margin-bottom: 1rem;
  color: var(--text-dark);
}

.tech-stack ul {
  list-style: none;
  padding: 0;
}

.tech-stack li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #dee2e6;
}

.tech-stack li:last-child {
  border-bottom: none;
}

.tech-stack strong {
  color: var(--secondary-color);
}

/* Responsive design */
@media (max-width: 768px) {
  .page {
    padding: 1rem;
  }
  
  .page-content {
    padding: 1.5rem;
  }
  
  .page h1 {
    font-size: 2rem;
  }
  
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .features-grid,
  .services-grid,
  .portfolio-grid {
    grid-template-columns: 1fr;
  }
}""",
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
    if file_info.get("is_json", False):
        content = json.dumps(file_info["content"], indent=2, ensure_ascii=False)
    else:
        content = file_info["content"]
    
    # Создаем файл
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Создан файл: {file_path}")

print("\n" + "="*50)
print("🎉 React + Vite проект успешно создан!")
print("="*50)
print("\n📋 Для запуска проекта выполните команды:")
print("npm install")
print("npm run dev")
print("\n🌐 Приложение будет доступно по адресу: http://localhost:3000")
print("\n✨ Особенности проекта:")
print("  • ⚡ Vite для молниеносной сборки")
print("  • ⚛️ React 18 с хуками")
print("  • 🍔 Адаптивное бургер-меню")
print("  • 📱 Полная мобильная поддержка")
print("  • 🎨 Современный дизайн с анимациями")
print("  • 🎯 Готовые страницы с контентом")