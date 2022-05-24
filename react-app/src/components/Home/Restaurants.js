import './Home.css';

import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';

import { favoriteOneRestaurant, unfavoriteOneRestaurant } from '../../store/session';

function Restaurants ({ restaurants, filter }) {
    const history = useHistory();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);

    return (
        <div id='restaurants'>
            <h1>{filter ? filter : "All Restaurants"}</h1>
            {
                filter === 'My Favorites' ?
                user.favorites.map(restaurant => (
                    <div className='restaurant' key={restaurant.id}>
                        {
                            user.favorites.find(favoriteRestaurant => favoriteRestaurant.id === restaurant.id) ?
                                <button className='faved' onClick={() => dispatch(unfavoriteOneRestaurant({ restaurantId: restaurant.id }))}><i className="fas fa-heart"></i></button>
                                :
                                <button className='unfaved' onClick={() => dispatch(favoriteOneRestaurant({ restaurantId: restaurant.id }))}><i className="far fa-heart"></i></button>
                        }
                        <img src={restaurant.picture} alt='' onClick={() => history.push(`/restaurant/${restaurant.id}`)}></img>
                        <p onClick={() => history.push(`/restaurant/${restaurant.id}`)}>{restaurant.name}</p>
                    </div>
                ))
                :
                restaurants.map(restaurant => (
                    !filter || filter === restaurant.category.name ? (<div className='restaurant' key={restaurant.restaurant.id}>
                        {
                            user.favorites.find(favoriteRestaurant => favoriteRestaurant.id === restaurant.id) ?
                                <button className='faved' onClick={() => dispatch(unfavoriteOneRestaurant({ restaurantId: restaurant.id }))}><i className="fas fa-heart"></i></button>
                                :
                                <button className='unfaved' onClick={() => dispatch(favoriteOneRestaurant({ restaurantId: restaurant.id }))}><i className="far fa-heart"></i></button>
                        }
                        <img src={restaurant.restaurant.picture} alt='' onClick={() => history.push(`/restaurant/${restaurant.restaurant.id}`)}></img>
                        <p onClick={() => history.push(`/restaurant/${restaurant.restaurant.id}`)}>{restaurant.restaurant.name}</p>
                    </div>) : null
                ))
            }
        </div>
    );
}

export default Restaurants;
