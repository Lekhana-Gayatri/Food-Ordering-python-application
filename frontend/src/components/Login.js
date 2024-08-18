// LoginPage.js
import React, { useState } from 'react';
import axios from 'axios';

const LoginPage = ({ API_URL, setToken }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const [error, setError] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post(`http://localhost:8000/login/`, {
                username,
                email,
                password
            });
            setToken(response.data.token); 
            console.log(response.data.key)  
            setError('');
            
        } catch (err) {
            setError('Invalid username or password',err);
        }
    };

    return (
        <div className="login-container row " class='content-container'>
            <h2 className='text-center pb-5'>Login</h2>
            {error && <p className="error">{error}</p>}
            <form onSubmit={handleSubmit}>
                <div className='row pb-3'>
                    <label htmlFor="username" className='col-3 pb-3'>Username</label>
                    <input className='col-6'
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className='row pb-3'>
                    <label htmlFor="email" className='col-3 pb-3'>Email</label>
                    <input className='col-6'
                        type="text"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className='row pb-3'>
                    <label htmlFor="password" className='col-3 pb-3'>Password</label>
                    <input
                    className='col-6'
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <div className='text-center'>
                <button className='btn btn-outline-primary' type="submit">Login</button>
                </div>
            </form>
        </div>
    );
};

export default LoginPage;
