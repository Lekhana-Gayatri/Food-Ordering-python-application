import React, { useState, useEffect } from 'react';
import { getRestaurants } from './api';
import axios from 'axios';
function RestaurantList(props) {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const data = await getRestaurants(props.token,props.API_URL);
        setRestaurants(data);
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    }
    fetchData();
  }, [props.token]);
  const handleCart = async (dishId) => {
    try {
        console.log(dishId, 1000000000000);

        // Send the dishId in the request body instead of the URL
        const response = await axios.post(`http://localhost:8000/cart/add_to_cart/${dishId}/`, {
            dish_id: dishId,    // Pass dishId in the request body
            quantity: 1         // You can adjust the quantity as needed
        }, {
            headers: {
                Authorization: `Bearer ${props.token}`
            }
        });

        console.log('Item added to cart:', response.data);
    } catch (error) {
        console.error('Error updating the cart:', error);
    }
};

  return (
    <div className="row">
      {restaurants.map((res) => (
        <div className="col-md-3 position-relative" key={res.id}>
          <div className="card mb-4 shadow-lg">
            {res.dish_img ? (
              <img
              src={`http://localhost:8000${res.dish_img}`}
                className="card-img-top"
                alt={res.dish_name}
                style={{ maxHeight: '150px', objectFit: 'cover' }}
              />
            ) : (
              <img
                src="path/to/default/image.jpg"
                className="card-img-top"
                alt="Default Image"
                style={{ maxHeight: '200px', objectFit: 'cover' }}
              />
            )}
            <div className="card-body">
            <h5 className="card-title">{res.dish_name}</h5>
              <p className="card-text">Price:  {res.price}</p>
              <p className="card-text">Restaurant:  {res.restaurant_name}</p>
              <p className="card-text">Discount:  {res.discount}</p>
            </div>
            <div className="d-flex justify-content-between mb-4 mx-3 my-3">
                <button
                  className="btn btn-success"
                   onClick={() => handleCart(res.id)}
                >
                  Add to Cart
                </button>
              </div>
          </div>
          <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
            {res.rating}
          </span>
        </div>
      ))}
    </div>
  );
}

export default RestaurantList;