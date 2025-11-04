import React, { useState } from 'react'

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

export default Contact