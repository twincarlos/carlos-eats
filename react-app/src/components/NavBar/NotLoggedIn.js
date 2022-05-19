import './NavBar.css';
import { NavLink } from 'react-router-dom';
import logo from '../../assets/logo.png';

function NotLoggedIn() {
    return (
        <nav id='not-logged-in'>
            <ul>
                <li>
                    <NavLink to='/splash' exact={true} activeClassName='active'>
                        <img style={{ width: 100 }} src={logo} alt=''></img>
                    </NavLink>
                </li>
                <li>
                    <NavLink id='login' to='/login' exact={true} activeClassName='active'>
                        Login
                    </NavLink>
                </li>
            </ul>
        </nav>
    );
}

export default NotLoggedIn;
