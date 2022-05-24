// constants
const SET_USER = 'session/SET_USER';
const REMOVE_USER = 'session/REMOVE_USER';

const ADD_CART = 'session/ADD_CART';
const DELETE_CART = 'session/DELETE_CART';

const ADD_NEW_CART_ITEM = 'session/ADD_NEW_CART_ITEM';
const ADD_EXISTING_CART_ITEM = 'session/ADD_EXISTING_CART_ITEM';
const UPDATE_CART_ITEM = 'session/UPDATE_CART_ITEM';
const DELETE_CART_ITEM = 'session/DELETE_CART_ITEM';

const ADD_NEW_ORDER = 'session/ADD_NEW_ORDER';

const FAVORITE_RESTAURANT = 'session/FAVORITE_RESTAURANT';
const UNFAVORITE_RESTAURANT = 'session/UNFAVORITE_RESTAURANT';

const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

const removeUser = () => ({
  type: REMOVE_USER,
});

const addCart = cart => ({
  type: ADD_CART,
  cart
});

const deleteCart = cartId => ({
  type: DELETE_CART,
  cartId
});

const addNewCartItem = cartItem => ({
  type: ADD_NEW_CART_ITEM,
  cartItem
});

const addExistingCartItem = cartItem => ({
  type: ADD_EXISTING_CART_ITEM,
  cartItem
});

const updateCartItem = cartItem => ({
  type: UPDATE_CART_ITEM,
  cartItem
});

const deleteCartItem = cartItem => ({
  type: DELETE_CART_ITEM,
  cartItem
});

const addNewOrder = order => ({
  type: ADD_NEW_ORDER,
  order
});

const favoriteRestaurant = restaurant => ({
  type: FAVORITE_RESTAURANT,
  restaurant
});

const unfavoriteRestaurant = restaurantId => ({
  type: UNFAVORITE_RESTAURANT,
  restaurantId
});

const initialState = { user: null };

export const authenticate = () => async (dispatch) => {
  const response = await fetch('/api/auth/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }

    dispatch(setUser(data));
  }
}

export const login = (email, password) => async (dispatch) => {
  const response = await fetch('/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email,
      password
    })
  });


  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data))
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ['An error occurred. Please try again.']
  }

}

export const logout = () => async (dispatch) => {
  const response = await fetch('/api/auth/logout', {
    headers: {
      'Content-Type': 'application/json',
    }
  });

  if (response.ok) {
    dispatch(removeUser());
  }
};


export const signUp = (username, email, password) => async (dispatch) => {
  const response = await fetch('/api/auth/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data))
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ['An error occurred. Please try again.']
  }
}

export const addNewCart = data => async dispatch => {
  const response = await fetch('/api/carts', {
    method: 'POST',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const cart = await response.json();
  dispatch(addCart(cart));
  return cart;
}

export const deleteOneCart = data => async dispatch => {
  const response = await fetch(`/api/carts/${data.cart_id}`, { method: 'DELETE' });
  const cartId = await response.json();
  dispatch(deleteCart(cartId));
}

export const addOneNewCartItem = data => async dispatch => {
  const response = await fetch(`/api/carts/${data.cart_id}/add_cart_item`, {
    method: 'POST',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  const cartItem = await response.json();
  dispatch(addNewCartItem(cartItem));
}

export const addOneExistingCartItem = data => async dispatch => {
  const response = await fetch(`/api/carts/${data.cart_id}/add_cart_item`, {
    method: 'PUT',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  const cartItem = await response.json();
  dispatch(addExistingCartItem(cartItem));
}

export const updateOneCartItem = data => async dispatch => {
  const response = await fetch(`/api/carts/${data.cart_id}/cart_item/${data.cart_item_id}`, {
    method: 'PUT',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  const cartItem = await response.json();
  dispatch(updateCartItem(cartItem));
}

export const deleteOneCartItem = data => async dispatch => {
  const response = await fetch(`/api/carts/${data.cart_id}/cart_item/${data.cart_item_id}`, { method: 'DELETE' });
  const cartItem = await response.json();
  dispatch(deleteCartItem(cartItem));
}

export const addOneNewOrder = data => async dispatch => {
  const response = await fetch('/api/orders', {
    method: 'POST',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  const order = await response.json();
  dispatch(addNewOrder(order));
}

export const favoriteOneRestaurant = data => async dispatch => {
  const response = await fetch(`/api/restaurants/favorite/${data.restaurantId}`, { method: 'POST' });
  const restaurant = await response.json();
  dispatch(favoriteRestaurant(restaurant));
}

export const unfavoriteOneRestaurant = data => async dispatch => {
  const response = await fetch(`/api/restaurants/favorite/${data.restaurantId}`, { method: 'DELETE' });
  const restaurantId = await response.json();
  dispatch(unfavoriteRestaurant(restaurantId))
}

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { user: action.payload }
    case REMOVE_USER:
      return { user: null }
    case ADD_CART:
      return {
        ...state,
        user: {
          ...state.user,
          carts: [...state.user.carts, action.cart]
        }
      }
    case DELETE_CART:
      return {
        ...state,
        user: {
          ...state.user,
          carts: state.user.carts.filter(cart => cart.id !== action.cartId)
        }
      }
    case ADD_NEW_CART_ITEM:
      return {
        ...state,
        user: {
          ...state.user,
          carts: state.user.carts.map(cart => {
            if (cart.id === action.cartItem.cart_id) {
              cart.cart_items = [...cart.cart_items, action.cartItem];
            }
            return cart;
          })
        }
      }
    case ADD_EXISTING_CART_ITEM:
      return {
        ...state,
        user: {
          ...state.user,
          carts: state.user.carts.map(cart => {
            if (cart.id === action.cartItem.cart_id) {
              cart.cart_items = cart.cart_items.map(cartItem => cartItem.id === action.cartItem.id ? action.cartItem : cartItem);
            }
            return cart;
          })
        }
      }
      case UPDATE_CART_ITEM:
        return {
          ...state,
          user: {
            ...state.user,
            carts: state.user.carts.map(cart => {
              if (cart.id === action.cartItem.cart_id) {
                cart.cart_items = cart.cart_items.map(cartItem => cartItem.id === action.cartItem.id ? action.cartItem : cartItem);
              }
              return cart;
            })
          }
        }
      case DELETE_CART_ITEM:
        return {
          ...state,
          user: {
            ...state.user,
            carts: state.user.carts.map(cart => {
              if (cart.id === action.cartItem.cart_id) {
                cart.cart_items = cart.cart_items.filter(cartItem => cartItem.id !== action.cartItem.cart_item_id);
              }
              return cart;
            })
          }
        }
      case ADD_NEW_ORDER:
        return {
          ...state,
          user: {
            ...state.user,
            orders: [...state.user.orders, action.order]
          }
        }
      case FAVORITE_RESTAURANT:
        return {
          ...state,
          user: {
            ...state.user,
            favorites: [...state.user.favorites, action.restaurant]
          }
        }
      case UNFAVORITE_RESTAURANT:
        return {
          ...state,
          user: {
            ...state.user,
            favorites: state.user.favorites.filter(restaurant => restaurant.id !== action.restaurantId)
          }
        }
    default:
      return state;
  }
}
