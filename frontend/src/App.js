import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { generateCharacter } from './apiService'; // Import api service

function App() {
  const [character, setCharacter] = useState(null);

  const handleGenerateCharacter = async() => {
    const specifications = { /* user specified options */ };
    try {
      const data = await generateCharacter(specifications);
      setCharacter(data.character);
    } catch (error) {
      console.error('Error generating character:', error);
    }
  };


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <button onClick={handleGenerateCharacter}>Generate Character</button>
        {character && <div>Generated Character: {character}</div>}
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
