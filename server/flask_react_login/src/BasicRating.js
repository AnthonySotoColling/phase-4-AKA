import React, { useState } from 'react';

export default function BasicRating({ userId, gameId }) {
  const [rating, setRating] = useState(0);

  const handleRatingChange = (event) => {
    setRating(event.target.value);
  };

  const handleSubmit = () => {
    if (rating > 0) {
      fetch('/api/ratings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: userId,
          game_id: gameId,
          rating: rating,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data.message);
        })
        .catch((error) => {
          console.error('Error saving rating:', error);
        });
    }
  };

  return (
    <div>
      <h4>Select Rating:</h4>
      <select value={rating} onChange={handleRatingChange}>
        <option value={0}>Select</option>
        <option value={1}>1</option>
        <option value={2}>2</option>
        <option value={3}>3</option>
        <option value={4}>4</option>
        <option value={5}>5</option>
      </select>
      <button onClick={handleSubmit}>Submit Rating</button>
    </div>
  );
}
