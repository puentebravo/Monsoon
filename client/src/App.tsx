import React from 'react';
import './App.css';
import BotSelector from './components/botSelector';
import Footer from './components/footer';
import Header from './components/header';

function App() {


  return (
    <div className='flex flex-col h-screen'>
    <Header/>
    <div className='mb-auto'>
    <BotSelector/>
    </div>
    <Footer/>
    </div>
  );
}

export default App;
