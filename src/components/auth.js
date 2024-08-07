import axios from 'axios';

const API_URL = 'http://localhost:8000/api/token/';

export const getToken = async (username, password) => {
  try {
    const response = await axios.post(API_URL, {
      username,
      password,
    });
    return response.data;
  } catch (error) {
    console.error('Error obtaining token:', error);
    throw error;
  }
};
