import React, { useContext, useRef, useState, useEffect } from "react";
import ReactDOM from "react-dom";
import "./Modal.css";

const ModalContext = React.createContext();

export function ModalProvider({ children }) {
  const modalRef = useRef();
  const [value, setValue] = useState();

  useEffect(() => {
    setValue(modalRef.current);
  }, []);

  return (
    <>
      <ModalContext.Provider value={value}>{children}</ModalContext.Provider>
      <div ref={modalRef} />
    </>
  );
}

export function Modal({ onClose, children, topStyle }) {
  const modalNode = useContext(ModalContext);
  if (!modalNode) return null;

  return ReactDOM.createPortal(
    <div id="modal" style={{ top: topStyle === 2 ? '9.5vh' : 0 }}>
      <div id="modal-background" onClick={onClose} style={{ top: topStyle === 2 ? '9.5vh' : 0 }} />
      <div id="modal-content">{children}</div>
    </div>,
    modalNode
  );
}
