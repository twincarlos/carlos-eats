import './Home.css';

import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { getAllRestaurants } from '../../store/restaurants';
import Categories from './Categories';
import Restaurants from './Restaurants';

function Home () {
    const dispatch = useDispatch();
    const restaurants = useSelector(state => state.restaurants.restaurants);
    const [loaded, setLoaded] = useState(false);
    const [filter, setFilter] = useState(null);

    useEffect(() => {
        (async () => await dispatch(getAllRestaurants()).then(() => setLoaded(true)))();
    }, [dispatch]);

    if (!loaded) return null;

    return (
        <div id='home'>
            <Categories categories={restaurants.slice(0, 4)} setFilter={setFilter}/>
            <Restaurants restaurants={restaurants} filter={filter}/>
        </div>
    );
}

export default Home;
