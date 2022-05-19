import './Splash.css';
import { NavLink } from 'react-router-dom';

function Splash() {
    return (
        <div id='splash'>
            <h1>Order food to your door</h1>
            <div id='address-form'>
                <input type='text' defaultValue='Miami, Fl'></input>
                <button>Find Food</button>
            </div>
            <p style={{ marginLeft: '2vw' }}><NavLink to='/login'>Login</NavLink> to see restauraunts in the area.</p>
        </div>
    );
}

export default Splash;
