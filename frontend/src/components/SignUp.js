// LoginPage.js
import React, { useState } from 'react';
import axios from 'axios';
import alert from './alert';
const RegisterPage = ({ API_URL, setToken }) => {
    const [username, setUsername] = useState('');
    const [password1, setPassword1] = useState(''); // Add state for password1
    const [password2, setPassword2] = useState('');
    const [email, setEmail] = useState('');
    const [text, setText] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post(`http://localhost:8000/register/`, {
                username,
                email,
                password1,
                password2
            }); 
            setText('Sign UP successful');
            
        } catch (err) {
            console.log(err)
            setError('response.data.non_field_errors');
        }
    };

    return (
        <div className="login-container row " class='content-container'>
            <h2 className='text-center pb-5'>Register</h2>
            {error && <alert text={error}/>}
            <alert text={text}/>
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
                    <label htmlFor="password1" className='col-3 pb-3'>Password1</label>
                    <input
                    className='col-6'
                        type="password"
                        id="password1"
                        value={password1}
                        onChange={(e) => setPassword1(e.target.value)}
                        required
                    />
                </div>
                <div className='row pb-3'>
                    <label htmlFor="password2" className='col-3 pb-3'>Password2</label>
                    <input
                    className='col-6'
                        type="password"
                        id="password2"
                        value={password2}
                        onChange={(e) => setPassword2(e.target.value)}
                        required
                    />
                </div>
                <div className='text-center'>
                <button className='btn btn-outline-primary' type="submit">Register</button>
                </div>
            </form>
        </div>
    );
};

export default RegisterPage;
