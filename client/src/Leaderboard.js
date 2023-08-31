import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
    const [games, setGames] = useState([]);

    useEffect(() => {
        const fetchLeaderboard = async () => {
            const response = await fetch('http://localhost:5555/api/leaderboard');
            const data = await response.json();
            setGames(data);
        };

        fetchLeaderboard();
    }, []);

    return (
        <div>
            <h1>Leaderboard</h1>
            <table>
                <thead>
                    <tr>
                        <th>Game Name</th>
                        <th>Genre</th>
                        <th>Average Rating</th>
                    </tr>
                </thead>
                <tbody>
                    {games.map(game => (
                        <tr key={game.id}>
                            <td>{game.name}</td>
                            <td>{game.genre}</td>
                            <td>{game.average_rating.toFixed(1)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Leaderboard;