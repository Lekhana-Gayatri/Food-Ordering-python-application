import axios from 'axios';

// const API_URL = 'http://localhost:8000/cart/';

export const getRestaurants = async (token,API_URL) => {
  try {
    console.log(API_URL,10000000000);
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
    console.log(dishId,1000000000000)

      const response = await axios.post(
          `${API_URL}add_to_cart/${dishId}/`,
          { quantity }, // Passing the quantity in the request body
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

// Function to remove an item from the cart
export const removeFromCart = async (token, API_URL, dishId) => {
  try {
      const response = await axios.post(
          `${API_URL}/remove_from_cart/${dishId}/`,
          {}, // No need for body, just triggering the removal
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
