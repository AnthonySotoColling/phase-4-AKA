import React, { useState, useEffect, useContext } from 'react';
import { UserIdContext } from './App';

function FavoritedGames() {
  const [favoritedGames, setFavoritedGames] = useState(null);
  const { userId } = useContext(UserIdContext);

  useEffect(() => {
    async function fetchFavorites() {
      try {
        const response = await fetch(`http://localhost:5555/api/favorites/${userId}`);
        const data = await response.json();
        if (Array.isArray(data)) {
          setFavoritedGames(data);
        } else {
          console.error('Unexpected server response:', data);
          setFavoritedGames([]); 
        }
      } catch (error) {
        console.error("Error fetching favorites:", error);
        setFavoritedGames([]); 
      }
    }

    if (userId) {
      fetchFavorites();
    }
  }, [userId]);

  const removeFavorite = async (gameId) => {
    try {
        const response = await fetch(`http://localhost:5555/api/favorites/${userId}/${gameId}`, {
            method: 'DELETE'
        });

        if (response.status === 200) {
            setFavoritedGames(prevGames => prevGames.filter(game => game.id !== gameId));
        } else {
            console.error("Failed to remove favorite");
        }

    } catch (error) {
        console.error("Error removing favorite:", error);
    }
}
  
return (
    <div>
        <h1>Favorited Games</h1>
        <ul>
            {favoritedGames && favoritedGames.map(game => (
                <li key={game.id}>
                    {game.name}
                    <button onClick={() => removeFavorite(game.id)}>Remove</button>
                </li>
            ))}
        </ul>
    </div>
);
}

export default FavoritedGames;
