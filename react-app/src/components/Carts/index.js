import './Carts.css';

import { useDispatch } from 'react-redux';

import { deleteOneCart, updateOneCartItem, deleteOneCartItem, addOneNewOrder } from '../../store/session';

function Carts({ carts }) {
    const dispatch = useDispatch();
    return (
        carts.length ?
        <div id='carts-main'>
            <h1>Your carts</h1>
            {
                carts.map(cart => (
                    <div key={cart.id} className='cart'>
                        <div id='restaurant-details'>
                            <img style={{ width: 100 }} src={cart.restaurant.picture} alt=''></img>
                            <p>{cart.restaurant.name}</p>
                        </div>
                        <div>
                            {
                                cart.cart_items.map(cartItem => (
                                    <div className='cart-item' key={cartItem.id}>
                                        <input type='number' defaultValue={cartItem.quantity} onChange={async e => {
                                            e.target.value > 0 ? dispatch(updateOneCartItem({ cart_id: cart.id, cart_item_id: cartItem.id, quantity: e.target.value })) : (cart.cart_items.length > 1 ? dispatch(deleteOneCartItem({ cart_id: cart.id, cart_item_id: cartItem.id })) : dispatch(deleteOneCart({ cart_id: cart.id })));
                                        }}></input>
                                        <p>{cartItem.item.name} ${cartItem.item.price * cartItem.quantity}</p>
                                    </div>
                                ))
                            }
                        </div>
                        <button onClick={async () => {
                            const now = new Date(Date.now());
                            const year = now.getFullYear();
                            const month = now.getMonth() + 1;
                            const date = now.getDate();
                            const hours = now.getHours();
                            const minutes = now.getMinutes();
                            const seconds = now.getSeconds();
                            const datetime = `${year}-${month < 10 ? `0${month}` : month}-${date < 10 ? `0${date}` : date} ${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}:${seconds < 10 ? `0${seconds}` : seconds}`;

                            await dispatch(addOneNewOrder({
                                restaurant_name: cart.restaurant.name,
                                restaurant_picture: cart.restaurant.picture,
                                time: datetime,
                                order_items: cart.cart_items.map(cartItem => ({ name: cartItem.item.name, price: cartItem.item.price, quantity: cartItem.quantity }))
                            })).then(() => dispatch(deleteOneCart({ cart_id: cart.id })));
                        }}>Checkout {cart.cart_items.reduce((prev, curr) => prev + (curr.quantity * curr.item.price), 0)}</button>
                    </div>
                ))
            }
        </div>
            :
        <div id='empty-cart'>
            <p>Add items from a restaurant to start a new cart</p>
        </div>
    );
}

export default Carts;
