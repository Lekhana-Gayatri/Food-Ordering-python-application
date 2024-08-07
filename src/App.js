// import './App.css';

// import React,{Component} from 'react';
// import NavBar from './components/NavBar';
// import News from './components/News';
// export default class App extends Component{
  
//   render(){
//     return(
//       <div>
//         <NavBar/>
//         <News pageSize={5}/>
//       </div>
//     );
//   }
// }
import React, { useState, useEffect } from 'react';
import NavBar from './components/NavBar';
import { getToken } from './components/auth';
import RestaurantList from './components/restaurantList';
import FoodList from './components/FoodList';
import Search from './components/SearchComponent';
import {
  BrowserRouter as Router,Routes,
  Route
} from 'react-router-dom';

function App() {
  const [data, setData] = useState([]);
  const [token, setToken] = useState(null);

  useEffect(() => {
    async function authenticateAndFetchData() {
      try {
        const authData = await getToken('lekhana', 'gayatri@18');
        setToken(authData.access);
      } catch (error) {
        console.error('Error obtaining token:', error);
      }
    }
    authenticateAndFetchData();
  }, []);
  

  // useEffect(() => {
  //   async function fetchData() {
  //     if (token) {
  //       try {
  //         const result = await getMyModels(token);
  //         setData(result);
  //       } catch (error) {
  //         console.error('Error fetching data:', error);
  //       }
  //     }
  //   }
  //   fetchData();
  // }, [token]);

  // return (
  //   <div>
  //     <h1>My Models</h1>
  //     <ul>
  //       {data.map(item => (
  //         <li key={item.pk}>{item.name}</li>
  //       ))}
  //     </ul>
  //   </div>
  // );
  return(<div><Router>
    <NavBar token={token}/>
     <Routes>
     <Route path="/Restaurants"element={<RestaurantList token={token} API_URL={'http://localhost:8000/res/0'} />}/>
     <Route path="/Food"element={<FoodList token={token} API_URL={'http://localhost:8000/dish/0'} />}/>
     </Routes>
  </Router>
  </div>
  );
}

export default App;
