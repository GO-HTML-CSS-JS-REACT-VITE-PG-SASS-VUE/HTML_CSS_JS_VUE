import React from 'react'

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

export default About