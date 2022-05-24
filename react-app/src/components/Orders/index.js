import './Orders.css';

import { useSelector } from 'react-redux';

function Orders() {
    const user = useSelector(state => state.session.user);

    return (
        <div id='orders-main'>
            <h1><i className="fas fa-receipt"></i> Your orders</h1>
            {
                user.orders.map(order => (
                    <div className='order' key={order.id}>
                        <img src={order.restaurant_picture} alt=''></img>
                        <div className='order-items'>
                            <h2>{order.restaurant_name}</h2>
                            {
                                order.order_items.map(orderItem => (
                                    <p key={orderItem.id}>
                                        {orderItem.quantity} X {orderItem.item_name} - ${orderItem.quantity * orderItem.item_price}
                                    </p>
                                ))
                            }
                            <p>Total: ${order.order_items.reduce((prev, curr) => prev + (curr.quantity * curr.item_price), 0)}</p>
                            <p>{order.time.slice(0, 16)}</p>
                        </div>
                    </div>
                ))
            }
        </div>
    );
}

export default Orders;
