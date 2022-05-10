const ALL_RESTAURANTS = 'restaurants/getAllRestaurants';

const allRestaurants = restaurants => ({
    type: ALL_RESTAURANTS,
    restaurants
});

const initialState = { restaurants: {} };

export const getAllRestaurants = () => async dispatch => {
    const response = await fetch('/api/restaurants');
    const restaurants = await response.json();
    dispatch(allRestaurants(restaurants.categories));
}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case ALL_RESTAURANTS:
            state.restaurants = action.restaurants;
            return state;
        default:
            return state;
    }
}
