import './Restaurants.css';

function Restaurants ({ restaurants, filter }) {
    return (
        <div id='restaurants'>
            {
                restaurants.map(restaurant => (
                    !filter || filter === restaurant.category.name ? (<div className='restaurant' key={restaurant.restaurant.id}>
                        <img src={restaurant.restaurant.picture} alt=''></img>
                        <p>{restaurant.restaurant.name}</p>
                    </div>) : null
                ))
            }
        </div>
    );
}

export default Restaurants;
