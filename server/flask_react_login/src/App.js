import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import './App.css';

function HomePage() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    async function fetchGames() {
      try {
        const response = await fetch('http://localhost:5555/api/games');
        const data = await response.json();
        setGames(data);
      } catch (error) {
        console.error("Error fetching games:", error);
      }
    }
    
    fetchGames();
  }, []);
  return (
    <div>
        <h1>Home Page</h1>
        <table>
            <thead>
                <tr>
                    <th>Game Name</th>
                    <th>Genre</th>
                    <th>Image</th>
                    <th>Rating</th>
                </tr>
            </thead>
            <tbody>
                {games.map(game => (
                    <tr key={game.id}>
                        <td>{game.name}</td>
                        <td>{game.genre}</td>
                        <td><img src={game.image} alt={game.name} width="100" /></td>
                        <td>
                            {game.average_rating ? game.average_rating.toFixed(1) : "No Ratings Yet"}
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
);
}

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

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
      setIsLoggedIn(true);
    } else {
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
    <BrowserRouter>
      <div className="App">
        <Routes>
          {/* If user is logged in, redirect them to home */}
          {isLoggedIn ? <Route path="*" element={<Navigate to="/home" replace />} /> : null}
  
          <Route path="/login" element={
            <div>
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
        } />

        <Route path="/home" element={<HomePage />} />

        {/* If user is not logged in, direct them to login */}
        {!isLoggedIn ? <Route path="*" element={<Navigate to="/login" replace />} /> : null}
      </Routes>
    </div>
  </BrowserRouter>
);
}

export default App;
