import React, { useState } from 'react';

export default function BasicRating({ userId, gameId }) {
  const [rating, setRating] = useState(0);
  const [submitted, setSubmitted] = useState(false);

  const handleRatingChange = (event) => {
    setRating(event.target.value);
  };

  const handleSubmit = () => {
    if (rating > 0) {
      fetch('http://localhost:5555/api/ratings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: userId,
          game_id: gameId,
          rating: parseInt(rating, 10) // to change the string into an integer
        }),
      })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
        .then((data) => {
          console.log(data.message);
          setSubmitted(true);
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
      <button onClick={handleSubmit} disabled={rating === 0 || submitted}>
        {submitted ? "Submitted!" : "Submit Rating"}
      </button>
    </div>
  );
}
