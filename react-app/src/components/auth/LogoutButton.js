import React from 'react';
import { useDispatch } from 'react-redux';
import { logout } from '../../store/session';

const LogoutButton = () => {
  const dispatch = useDispatch()
  const onLogout = async (e) => {
    await dispatch(logout());
  };

  return <button style={{
    border: 'none',
    backgroundColor: '#EEEEEE',
    padding: '10px 20px',
    borderRadius: 20
  }} onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
