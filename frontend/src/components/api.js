import axios from 'axios';

export const getRestaurants = async (token,API_URL) => {
  try {
    const response = await axios.get(API_URL, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    console.log(response.data);
    return response.data;
  } catch (error) {

    console.error('Error fetching data:', error);
    throw error;
  }
};

export const addToCart = async (token, API_URL, dishId, quantity) => {
  try {

      const response = await axios.post(
          `${API_URL}add_to_cart/${dishId}/`,
          { quantity },
          {
              headers: {
                  'Authorization': `Bearer ${token}`,
                  'Content-Type': 'application/json',
              },
          }
      );
      return response.data;
  } catch (error) {
      throw new Error('Error adding item to the cart.');
  }
};

export const removeFromCart = async (token, API_URL, dishId) => {
  try {
      const response = await axios.post(
          `${API_URL}/remove_from_cart/${dishId}/`,
          {}, 
          {
              headers: {
                  'Authorization': `Bearer ${token}`,
                  'Content-Type': 'application/json',
              },
          }
      );
      return response.data;
  } catch (error) {
      throw new Error('Error removing item from the cart.');
  }
};
