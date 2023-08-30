import React, { useState } from 'react';
import './LoginStyles.css';

function LoginForm() {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:5555/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams(formData) // formData already contains the username and password
            });
    
            const data = await response.json();
    
            if(response.status === 200) {
                console.log("Login successful:", data);
                // Handle successful login, maybe redirect to dashboard, store token, etc.
            } else {
                console.error("Error:", data.message);
                // Handle login error, maybe show a message to the user
            }
        } catch (err) {
            console.error("Failed to fetch:", err);
            // Handle fetch error, maybe show a message to the user
        }
    };
    

    return (
        <div className="login-container">
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input 
                        type="text" 
                        name="username" 
                        value={formData.username} 
                        onChange={handleChange} 
                    />
                </label>
                <label>
                    Password:
                    <input 
                        type="password" 
                        name="password" 
                        value={formData.password} 
                        onChange={handleChange} 
                    />
                </label>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default LoginForm;
