import React, { useState } from 'react';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:5555/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (response.status === 200) {
      setMessage(data.message);
    }else {
      setMessage(data.message);
    }
  };

  const handleRegister = async () => {
    const response = await fetch('http://localhost:5555/api/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
  
    const data = await response.json();
  
    if (response.status === 201) {
      setMessage("Registration successful! Please log in.");
    } else {
      setMessage(data.message);
    }
  };
  

  return (
    <div className="App">
      <h1>Login</h1>
      {message && <p style={{color: message === "Invalid credentials!" ? 'red' : 'green'}}>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username: </label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label>Password: </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
      <button onClick={handleRegister}>Would you like to create an account?</button>
    </div>
  );
}

export default App;
