import React from 'react'

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

export default Portfolio