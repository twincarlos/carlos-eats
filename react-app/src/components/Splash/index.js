import './Splash.css';
import { useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';

function Splash() {
    const history = useHistory();
    const user = useSelector(state => state.session.user);

    return (
        <div id='splash'>
            <h1>Order food to your door</h1>
            <div id='address-form'>
                <input type='text' defaultValue='Miami, Fl'></input>
                <button onClick={() => history.push(user ? '/' : '/login')}>Find Food</button>
            </div>
            { !user && <p style={{ marginLeft: '2vw' }}><NavLink to='/login'>Login</NavLink> to see restauraunts in the area.</p> }
        </div>
    );
}

export default Splash;
