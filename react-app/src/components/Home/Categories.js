import './Home.css';
import allRestaurants from '../../assets/allRestaurants.png';
import myFavorites from '../../assets/myFavorites.png';

function Categories ({ categories, setFilter }) {

    return (
        <div id='categories'>
            <div className='category' onClick={() => setFilter(null)}>
                <img src={allRestaurants} alt=''></img>
                <p>All Restaurants</p>
            </div>
            <div className='category' onClick={() => setFilter('My Favorites')}>
                <img src={myFavorites} alt=''></img>
                <p>My Favorites</p>
            </div>
            {
                categories.map(category => (
                    <div className='category' key={category.category.id} onClick={() => setFilter(category.category.name)}>
                        <img src={category.category.picture} alt=''></img>
                        <p>{category.category.name}</p>
                    </div>
                ))
            }
        </div>
    );
}

export default Categories;
