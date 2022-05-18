// constants
const SET_USER = 'session/SET_USER';
const REMOVE_USER = 'session/REMOVE_USER';

const ADD_CART = 'session/ADD_CART';
const ADD_NEW_CART_ITEM = 'session/ADD_NEW_CART_ITEM';
const ADD_EXISTING_CART_ITEM = 'session/ADD_EXISTING_CART_ITEM';

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

const addNewCartItem = cartItem => ({
  type: ADD_NEW_CART_ITEM,
  cartItem
});

const addExistingCartItem = cartItem => ({
  type: ADD_EXISTING_CART_ITEM,
  cartItem
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
    default:
      return state;
  }
}
