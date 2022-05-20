import React from 'react';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { Modal } from '../../context/Modal';
import Carts from '../Carts';
import Search from '../Search';
import './NavBar.css';

import logo from '../../assets/logo.png';

const LoggedIn = ({ user }) => {
  const [showModal, setShowModal] = useState(null);
  const [results, setResults] = useState([]);

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
          <input onFocus={() => setShowModal(2)} type='text' placeholder='Food, groceries, drinks, etc' onChange={async e => {
            if (e.target.value.length) {
              await fetch(`/api/restaurants/search/${e.target.value}`).then(async result => {
                const response = await result.json();
                setResults(response.restaurants);
              });
            } else {
              setResults([]);
            }
          }}></input>
        </li>
        <li>
          <button id='cart' onClick={() => setShowModal(1)}>Cart</button>
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
        showModal && <Modal onClose={() => setShowModal(null)} topStyle={showModal}>
          {showModal === 1 ? <Carts carts={user.carts} /> : <Search results={results} setShowModal={setShowModal} />}
        </Modal>
      }
    </nav>
  );
}

export default LoggedIn;
