import React, { useState, useEffect, useContext } from 'react';
import { UserIdContext } from './App'; 

const HomePage = () => {
    const [games, setGames] = useState([]);
    const userId = useContext(UserIdContext);


    useEffect(() => {
        const fetchGames = async () => {
            const response = await fetch('http://localhost:5555/api/games');
            const data = await response.json();
            setGames(data);
        };

        fetchGames();
    }, []);

    const toggleFavorite = async (game_id) => {
        const response = await fetch('http://localhost:5555/api/favorites', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId, game_id }),
        });

        const data = await response.json();
        console.log(data.message);
    };

    return (
        <div>
            <h1>Games List</h1>
            <ul>
                {games.map(game => (
                    <li key={game.id}>
                        {game.name} - Rated: {game.rating}
                        <button onClick={() => toggleFavorite(game.id)}>Favorite</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default HomePage;