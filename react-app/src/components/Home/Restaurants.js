import './Home.css';

import { useHistory } from 'react-router-dom';

function Restaurants ({ restaurants, filter }) {
    const history = useHistory();

    return (
        <div id='restaurants'>
            {
                restaurants.map(restaurant => (
                    !filter || filter === restaurant.category.id ? (<div className='restaurant' key={restaurant.restaurant.id} onClick={() => history.push(`/restaurant/${restaurant.restaurant.id}`)}>
                        <img src={restaurant.restaurant.picture} alt=''></img>
                        <p>{restaurant.restaurant.name}</p>
                    </div>) : null
                ))
            }
        </div>
    );
}

export default Restaurants;
