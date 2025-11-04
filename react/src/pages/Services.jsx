import React from 'react'

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

export default Services