import React, { useState, useEffect } from 'react'
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

export default App