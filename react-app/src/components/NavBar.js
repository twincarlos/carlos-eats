import React from 'react';
import { useState } from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import { Modal } from '../context/Modal';
import Carts from './Carts';

const NavBar = () => {
  const user = useSelector(state => state.session.user);
  const [showModal, setShowModal] = useState(false);

  return (
    <nav>
      <ul>
        <li>
          <NavLink to='/' exact={true} activeClassName='active'>
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to='/login' exact={true} activeClassName='active'>
            Login
          </NavLink>
        </li>
        <li>
          <NavLink to='/sign-up' exact={true} activeClassName='active'>
            Sign Up
          </NavLink>
        </li>
        <li>
          <NavLink to='/users' exact={true} activeClassName='active'>
            Users
          </NavLink>
        </li>
        <li>
          <button onClick={() => setShowModal(true)}>Cart</button>
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

export default NavBar;
