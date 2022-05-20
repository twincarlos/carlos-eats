import React from 'react';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { Modal } from '../../context/Modal';
import Carts from '../Carts';
import './NavBar.css';

import logo from '../../assets/logo.png';

const LoggedIn = ({ user }) => {
  const [showModal, setShowModal] = useState(false);

  return (
    <nav id='logged-in'>
      <ul>
        <li>
          <NavLink to='/' exact={true} activeClassName='active'>
            <img style={{ width: 100 }} src={logo} alt=''></img>
          </NavLink>
        </li>
        <li id='address'>
          { user.address }
        </li>
        <li>
          <input type='text' placeholder='Food, groceries, drinks, etc'></input>
        </li>
        <li>
          <button id='cart' onClick={() => setShowModal(true)}>Cart</button>
        </li>
        <li>
          <NavLink className='nav-links' to='/orders'>
            Orders
          </NavLink>
        </li>
        <li>
          <LogoutButton />
        </li>
      </ul>
      {
        showModal && <Modal onClose={() => setShowModal(false)}>
          <Carts carts={user.carts} />
        </Modal>
      }
    </nav>
  );
}

export default LoggedIn;
