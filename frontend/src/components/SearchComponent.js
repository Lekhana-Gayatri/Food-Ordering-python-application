import React, { useState } from 'react';
import { searchDishes } from './searchApi';

function SearchComponent({ token }) {
  const [query, setQuery] = useState('');
  const [dishes, setDishes] = useState([]);

  const handleSearch = async () => {
    try {
      const results = await searchDishes(query, token);
      setDishes(results.dishes || []);
       // Ensure results.dishes is assigned
       
    } catch (error) {
      console.error('Error during search:', error);
      setDishes([]); // Set dishes to an empty array in case of error
    }
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search dishes..."
      />
      <button onClick={handleSearch}>Search</button>
      <div className="row">
        {dishes && dishes.map((dish) => (
          <div className="col-md-4 position-relative" key={dish.id}>
            <div className="card mb-4 shadow-lg">
              {dish.dish_img ? (
                <img
                  src={dish.dish_img.url}
                  className="card-img-top"
                  alt={dish.dish_name}
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
                <h5 className="card-title">{dish.dish_name}</h5>
                <p className="card-text">{dish.price}</p>
                <p className="card-text">{dish.description}</p>
              </div>
            </div>
            <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
              {dish.rating}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SearchComponent;


// import NewsItem from './NewsItem'
// import Spinner from './Spinner'
// export class News extends Component {
//     articles = [];
//     constructor() {
//         super();
//         this.state = {
//             articles: this.articles,
//             loading: false,
//             page: 1
//         }
//     }
//     handleNextclick = async () => {
//         if(!(this.state.page+1>Math.ceil(this.state.totalResults/this.props.pageSize))){
//             console.log("nextS")
//             let url = `
//             https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7627980e817944c8aa911268b7b7a8e3&page=${this.state.page + 1}&pageSize=${this.props.pageSize}`
//             let data = await fetch(url);
//             let parseData = await data.json();
//             this.setState({ page: this.state.page + 1, articles: parseData.articles })
//         }
//     }
//     handleprevclick = async () => {
//         console.log("pre")
//         let url = `
//         https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7627980e817944c8aa911268b7b7a8e3&page=${this.state.page - 1}&pageSize=${this.props.pageSize}`
//         let data = await fetch(url);
//         let parseData = await data.json();
//         this.setState({ page: this.state.page - 1, articles: parseData.articles })
//     }

//     async componentDidMount() {
//         let url = `https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7627980e817944c8aa911268b7b7a8e3&pageSize=${this.props.pageSize}`
//         let data = await fetch(url);
//         let parseData = await data.json();
//         this.setState({ articles: parseData.articles })
//     }

//     render() {
//         return (
//             <div >
//                 <div className="container my-3">
//                     <h2>NewsMonkey - Top Headlines</h2>
//                     {this.state.loading && <Spinner/>}
//                     <div className="row">
//                         {this.state.articles.map((element) => {
//                             return (
//                                 <div className='col-md-4' key={element.url}>
//                                     <NewsItem title={element.title} description={element.description} imageUrl={element.urlToImage} newsUrl={element.url} />
//                                 </div>
//                             );
//                         })}
//                     </div></div>
//                 <div style={{ display: 'flex', justifyContent: 'space-between', padding: '100px' }}>
//                     <button className="btn btn-primary" disabled={this.page <= 1} onClick={this.handleprevclick}>&larr; Previous</button>
//                     <button className="btn btn-primary" disabled={(this.state.page+1>Math.ceil(this.state.totalResults/this.props.pageSize))} onClick={this.handleNextclick}>Next &rarr;</button>
//                 </div>
//             </div>
//         )
//     }
// }

//export default dishes
