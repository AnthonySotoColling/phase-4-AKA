import React, { useState, useEffect, createContext, useContext } from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import './App.css';
import HomePage from './homePage';
import BasicRating from './BasicRating';

export const UserIdContext = createContext();

function LocalHomePage() {
  const [games, setGames] = useState([]);
  const { userId } = useContext(UserIdContext);
  console.log("userId in LocalHomePage:", userId);

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

  function isFavorited(gameId) {
    return false;
  }
  
  async function toggleFavorite(game_id) {
  if (!userId) {
    console.error("User is not logged in or userId is missing.");
    return;
  }

  try {
    const response = await fetch('http://localhost:5555/api/favorites', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user_id: userId, game_id }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data.message);
  } catch (error) {
    console.error("Failed to toggle favorite:", error);
  }
}


return (
  <div>
    <h1>Your Games</h1> 
    <table>
      <thead>
        <tr>
          <th>Game Name</th>
          <th>Genre</th>
          <th>Image</th>
          <th>Rating</th>
          <th>Your Rating</th> {/* New Column for User's Rating */}
          <th>Actions</th> 
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
            <td>
              {userId && <BasicRating userId={userId} gameId={game.id} />} {/* Rating Component */}
            </td>
            <td>
              <button 
                onClick={() => toggleFavorite(game.id)} 
                style={isFavorited(game.id) ? { backgroundColor: 'yellow' } : {}}
              >
                {isFavorited(game.id) ? 'Unfavorite' : 'Favorite'}
              </button>
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
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem("token"));
  const initialUserId = localStorage.getItem("userId");
  console.log("Initial userId from localStorage:", initialUserId);
  const [userId, setUserId] = useState(initialUserId);
  console.log("Initial userId:", userId);


  const handleLogin = async (e) => {
    e.preventDefault();
  
    const response = await fetch('http://localhost:5555/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
  
    const data = await response.json();
  
    if (response.status === 200) {
      console.log("Received userId from server:", data.user_id);
      setMessage(data.message);
      setIsLoggedIn(true);
      localStorage.setItem("token", data.access_token);
      setUserId(data.user_id);
      localStorage.setItem("userId", data.user_id);  
    }
     else {
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
    <UserIdContext.Provider value={{ userId, setUserId }}>
      <BrowserRouter>
        <div className="App">
          <Routes>
            <Route path="/login" element={
              isLoggedIn ? 
                <Navigate to="/home" replace /> :
                (
                  <div>
                    <h1>Login</h1>
                    {message && <p style={{color: message === "Invalid credentials!" ? 'red' : 'green'}}>{message}</p>}
                    <form onSubmit={handleLogin}> 
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
                )
            } />
    
            <Route path="/home" element={
              isLoggedIn ? 
                <LocalHomePage /> : 
                <Navigate to="/login" replace />
            } />
          </Routes>
        </div>
      </BrowserRouter>
    </UserIdContext.Provider>
  );
}
  
  export default App;
  
  
