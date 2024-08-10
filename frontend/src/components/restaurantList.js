import React, { useState, useEffect } from 'react';
import { getRestaurants } from './api';

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

  return (
    <div className="row">
      {restaurants.map((res) => (
        <div className="col-md-3 position-relative" key={res.id}>
          <div className="card mb-4 shadow-lg">
            {res.rimg ? (
              <img
              src={`http://localhost:8000${res.rimg}`}
                className="card-img-top"
                alt={res.name}
                style={{ maxHeight: '200px', objectFit: 'cover' }}
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
            <a href={`/dishes/${res.id}`}><h5 className="card-title">{res.name}</h5></a>
              <p className="card-text">{res.address}</p>
              <p className="card-text">Closing Time: {res.closing_time}</p>
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
