import './Restaurant.css';

import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';

import { addNewCart, addOneNewCartItem, addOneExistingCartItem } from '../../store/session';

function ItemModal({ item }) {
    const restaurantId = Number(useParams().restaurantId);
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const [quantity, setQuantity] = useState(1);

    const handleSubmit = async e => {
        e.preventDefault();
        let itemFound = null;
        const cartFound = user.carts.find(userCart => {
            if (userCart.restaurant.id === restaurantId) {
                itemFound = userCart.cart_items.find(cartItem => cartItem.item.id === item.id);
                return true;
            }
            return false;
        });
        if (cartFound) {
            if (itemFound) {
                dispatch(addOneExistingCartItem({
                    cart_item_id: itemFound.id,
                    cart_id: cartFound.id,
                    item_id: item.id,
                    quantity
                }));
            } else {
                dispatch(addOneNewCartItem({
                    cart_id: cartFound.id,
                    item_id: item.id,
                    quantity
                }));
            }
        } else {
            await dispatch(addNewCart({ restaurant_id: restaurantId })).then(cart => dispatch(addOneNewCartItem({
                cart_id: cart.id,
                item_id: item.id,
                quantity
            })));
        }
    }

    return (
        <div id='item-modal'>
            <img src={item.picture} alt=''></img>
            <h1>{item.name}</h1>
            <h4>{item.price}</h4>
            <p>{item.description}</p>
            <form onSubmit={handleSubmit} style={{ display: 'flex' }}>
                <input type='number' value={quantity} onChange={e => setQuantity(Number(e.target.value))}></input>
                <button>Add to Cart</button>
                <p>${item.price * quantity}</p>
            </form>
        </div>
    );
}

export default ItemModal;
