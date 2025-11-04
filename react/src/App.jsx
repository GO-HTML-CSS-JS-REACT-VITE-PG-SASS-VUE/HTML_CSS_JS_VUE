import React, { useState } from 'react'
import BurgerMenu from './components/BurgerMenu'
import Home from './pages/Home'
import About from './pages/About'
import Services from './pages/Services'
import Portfolio from './pages/Portfolio'
import Contact from './pages/Contact'
import './App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('home')

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