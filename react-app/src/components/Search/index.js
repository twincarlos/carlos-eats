import './Search.css';

import { useHistory } from 'react-router-dom';

function Search({ results, setShowModal }) {
    const history = useHistory();

    return (
        <div id='search-modal'>
            {
                results.map(restaurant => (
                    <div className='restaurant-search' key={restaurant.id} onClick={() => {
                        history.push(`/restaurant/${restaurant.id}`);
                        setShowModal(null);
                    }}>
                        <img src={restaurant.picture} alt=''></img>
                        <p>{restaurant.name}</p>
                    </div>
                ))
            }
        </div>
    );
}

export default Search;
