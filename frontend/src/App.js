import React, { useState } from 'react';
import './App.css';
import { generateCharacter } from './apiService'; // Import api service

function App() {
  const [character, setCharacter] = useState(null);

  const handleGenerateCharacter = async() => {
    const specifications = { /* user specified options */ };
    try {
      const data = await generateCharacter(specifications);
      console.log(data);
      setCharacter(data);
    } catch (error) {
      console.error('Error generating character:', error);
    }
  };

  //having one row and a column class in case decided later on for multiple columns
  return (
    <div className="App">
    <div className="container">
      <div className="settings">
        <h2>Settings</h2>
        <div className="checkbox-group">
          <label>
            <input type="checkbox" /> Random Name
          </label>
          <label>
            <input type="checkbox" /> Random Class
          </label>
          <label>
            <input type="checkbox" /> Random Race
          </label>
          <label>
            <input type="checkbox" /> Random Alignment
          </label>
        </div>
        <button onClick={handleGenerateCharacter}>Generate Character</button>
      </div>
      <div className="character-content">
        {character ? (
          <div className="character-details">
            <h2 className="generated-header">Generated Character</h2>
            <p><strong>Name:</strong> {character.name}</p>
            <p><strong>Class:</strong> {character.class}</p>
            <p><strong>Subclass:</strong> {character.subclass}</p>
            <p><strong>Race:</strong> {character.race}</p>
            <p><strong>Alignment:</strong> {character.alignment}</p>
          </div>
        ) : (
          <p className="placeholder">Your generated character will appear here...</p>
        )}
      </div>
    </div>
  </div>
  );
}

export default App;
