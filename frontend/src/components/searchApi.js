import axios from 'axios';

const SEARCH_API_URL = 'http://localhost:8000/search/';

export const searchDishes = async (query, token) => {
  try {
    const response = await axios.get(SEARCH_API_URL, {
      params: { query },
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    return response.data.dishes; // Ensure the API returns data in a format that this matches
  } catch (error) {
    console.error('Error searching dishes:', error);
    throw error;
  }
};


// import React, { useState } from 'react';
// import { dishes } from './News';

// function Search({ token, query}) {
//   const [searchQuery, setSearchQuery] = useState(query || '');
//   const [results, setResults] = useState([]);

//   const handleSearch = async () => {
//     try {
//       const data = await dishes(searchQuery, token);
//       setResults(data.dishes);
//     } catch (error) {
//       console.error('Error during search:', error);
//     }
//   };

//   return (
//     <div>
//       <input
//         type="text"
//         value={searchQuery}
//         onChange={(e) => setSearchQuery(e.target.value)}
//         placeholder="Search dishes..."
//       />
//       <button onClick={handleSearch}>Search</button>
//       <ul>
//         {results.map((dish) => (
//           <li key={dish.id}>{dish.name} - ${dish.price}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }

export default searchDishes;
