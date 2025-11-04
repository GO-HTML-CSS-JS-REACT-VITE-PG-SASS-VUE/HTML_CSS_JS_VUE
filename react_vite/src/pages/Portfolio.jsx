import React from 'react'

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

export default Portfolio