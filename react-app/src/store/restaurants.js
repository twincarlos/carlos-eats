const ALL_RESTAURANTS = 'restaurants/getAllRestaurants';
const ONE_RESTAURANT = 'restaurants/getOneRestaurant';

const allRestaurants = restaurants => ({
    type: ALL_RESTAURANTS,
    restaurants
});

const oneRestaurant = restaurant => ({
    type: ONE_RESTAURANT,
    restaurant
});

const initialState = { restaurants: {}, restaurant: {} };

export const getAllRestaurants = () => async dispatch => {
    const response = await fetch('/api/restaurants');
    const restaurants = await response.json();
    dispatch(allRestaurants(restaurants.categories));
}

export const getOneRestaurant = (restaurantId) => async dispatch => {
    const response = await fetch(`/api/restaurants/${restaurantId}`);
    const restaurant = await response.json();
    dispatch(oneRestaurant(restaurant));
}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case ALL_RESTAURANTS:
            state.restaurants = action.restaurants;
            return state;
        case ONE_RESTAURANT:
            state.restaurant = action.restaurant;
            return state;
        default:
            return state;
    }
}
