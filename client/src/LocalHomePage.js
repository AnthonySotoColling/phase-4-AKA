// import React, { useState, useEffect, useContext } from 'react';
// import GameRow from './GameRow';
// import { UserIdContext } from './UserIdContext';

// function LocalHomePage() {
//     const [games, setGames] = useState([]);
//     const { userId } = useContext(UserIdContext);
//     console.log("userId in LocalHomePage:", userId);
  
//     useEffect(() => {
//       async function fetchGames() {
//         try {
//           const response = await fetch('http://localhost:5555/api/games');
//           const data = await response.json();
//           setGames(data);
//         } catch (error) {
//           console.error("Error fetching games:", error);
//         }
//       }
      
//       fetchGames();
//     }, []);
  
//     function isFavorited(gameId) {
//       return false;
//     }
    
//     async function toggleFavorite(game_id) {
//     if (!userId) {
//       console.error("User is not logged in or userId is missing.");
//       return;
//     }
  
//     try {
//       const response = await fetch('http://localhost:5555/api/favorites', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ user_id: userId, game_id }),
//       });
  
//       if (!response.ok) {
//         throw new Error(`HTTP error! Status: ${response.status}`);
//       }
  
//       const data = await response.json();
//       console.log(data.message);
//     } catch (error) {
//       console.error("Failed to toggle favorite:", error);
//     }
// }

// return (
//     <div>
//       <h1>Your Games</h1> 
//       <table>
//         <thead>
//           <tr>
//             <th>Game Name</th>
//             <th>Genre</th>
//             <th>Image</th>
//             <th>Rating</th>
//             <th>Your Rating</th> 
//             <th>Actions</th> 
//           </tr>
//         </thead>
//         <tbody>
//           {games.map(game => (
//             <tr key={game.id}>
//               <td>{game.name}</td>
//               <td>{game.genre}</td>
//               <td><img src={game.image} alt={game.name} width="100" /></td>
//               <td>
//                 {game.average_rating ? game.average_rating.toFixed(1) : "No Ratings Yet"}
//               </td>
//               <td>
//                 {userId && <BasicRating userId={userId} gameId={game.id} />} 
//               </td>
//               <td>
//                 <button 
//                   onClick={() => toggleFavorite(game.id)} 
//                   style={isFavorited(game.id) ? { backgroundColor: 'yellow' } : {}}
//                 >
//                   {isFavorited(game.id) ? 'Unfavorite' : 'Favorite'}
//                 </button>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// }