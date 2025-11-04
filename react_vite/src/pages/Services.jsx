import React from 'react'

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

export default Services