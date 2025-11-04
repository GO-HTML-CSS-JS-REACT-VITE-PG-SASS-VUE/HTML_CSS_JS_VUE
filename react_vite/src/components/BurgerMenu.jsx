import React, { useState, useEffect } from 'react'
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

export default BurgerMenu