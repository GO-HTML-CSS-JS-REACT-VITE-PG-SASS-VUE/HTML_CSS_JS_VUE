import React from 'react'

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

export default Contact