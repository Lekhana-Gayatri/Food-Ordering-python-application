import axios from 'axios';

//const API_URL = 'http://localhost:8000/res/';

export const getRestaurants = async (token,API_URL) => {
  try {
    const response = await axios.get(API_URL, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};
