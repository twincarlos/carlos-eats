import './Carts.css';

import { useDispatch } from 'react-redux';

import { deleteOneCart, updateOneCartItem, deleteOneCartItem } from '../../store/session';

function Carts({ carts }) {
    const dispatch = useDispatch();
    return (
        <div id='carts-main'>
            {
                carts.map(cart => (
                    <div key={cart.id} className='cart' style={{ display: 'flex' }}>
                        <div>
                            <img style={{ width: 100 }} src={cart.restaurant.picture} alt=''></img>
                            <p>{cart.restaurant.name}</p>
                        </div>
                        <div>
                            {
                                cart.cart_items.map(cartItem => (
                                    <div key={cartItem.id} style={{ display: 'flex' }}>
                                        <input type='number' defaultValue={cartItem.quantity} onChange={async e => {
                                            e.target.value > 0 ? dispatch(updateOneCartItem({ cart_id: cart.id, cart_item_id: cartItem.id, quantity: e.target.value })) : (cart.cart_items.length > 1 ? dispatch(deleteOneCartItem({ cart_id: cart.id, cart_item_id: cartItem.id })) : dispatch(deleteOneCart({ cart_id: cart.id })));
                                        }}></input>
                                        <p>{cartItem.item.name} ${cartItem.item.price * cartItem.quantity}</p>
                                    </div>
                                ))
                            }
                        </div>
                        <button>Checkout {cart.cart_items.reduce((prev, curr) => prev + (curr.quantity * curr.item.price), 0)}</button>
                    </div>
                ))
            }
        </div>
    );
}

export default Carts;
