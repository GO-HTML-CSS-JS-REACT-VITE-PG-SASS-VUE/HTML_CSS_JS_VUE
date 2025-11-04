import React, { useState } from 'react'
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

export default BurgerMenu