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
        <div>
          <li>
            <NavLink to='/' exact={true} activeClassName='active'>
              <img style={{ width: 100 }} src={logo} alt=''></img>
            </NavLink>
          </li>
        </div>
        <div>
          <li>
            <input style={{ width: showModal === 2 ? 600 : 200 }} onFocus={() => setShowModal(2)} type='text' placeholder='Food, groceries, drinks, etc' onChange={async e => {
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
        </div>
        <div>
          <li>
            <button id='cart' onClick={() => setShowModal(1)}><i className="fas fa-shopping-cart"></i> Cart</button>
          </li>
          <li>
            <NavLink className='nav-links' to='/orders'>
              <i className="fas fa-receipt"></i> Orders
            </NavLink>
          </li>
          <li>
            <LogoutButton />
          </li>
        </div>
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
