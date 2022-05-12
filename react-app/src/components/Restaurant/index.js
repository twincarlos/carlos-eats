import './Restaurant.css';

import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';

import { getOneRestaurant } from '../../store/restaurants';
import Items from './Items';
import ItemSections from './ItemSections';

function Restaurant () {
    const dispatch = useDispatch();
    const [loaded, setLoaded] = useState(false);
    const restaurantId = useParams().restaurantId;
    const restaurant = useSelector(state => state.restaurants.restaurant);
    const [currentSection, setCurrentSection] = useState(null);

    useEffect(() => {
        (async () => await dispatch(getOneRestaurant(restaurantId)).then(() => setLoaded(true)))();
    }, [dispatch, restaurantId]);

    if (!loaded) return null;

    return (
        <div id='restaurant'>
            <img src={restaurant.picture} alt=''></img>
            <h1>{restaurant.name}</h1>
            <div id='menu'>
                <ItemSections itemSections={restaurant.menu_sections} setCurrentSection={setCurrentSection} />
                <Items itemSections={restaurant.menu_sections} currentSection={currentSection} />
            </div>
        </div>
    );
}

export default Restaurant;
