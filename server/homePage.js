import React, { useState, useEffect } from 'react';

const HomePage = () => {
    const [games, setGames] = useState([]);

    useEffect(() => {
        const fetchGames = async () => {
            const response = await fetch('http://localhost:5555/api/games');
            const data = await response.json();
            setGames(data);
        };

        fetchGames();
    }, []);

    return (
        <div>
            <h1>Games List</h1>
            <ul>
                {games.map(game => (
                    <li key={game.id}>
                        {game.name} - Rated: {game.rating}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default HomePage;