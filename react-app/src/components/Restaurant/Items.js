import './Restaurant.css';

import { useState } from 'react';
import { Modal } from '../../context/Modal';
import ItemModal from './ItemModal';

function Items ({ itemSections, currentSection }) {
    const [showModal, setShowModal] = useState(null);

    return (
        <div id='items'>
            {
                showModal && <Modal onClose={() => setShowModal(null)}>
                    <ItemModal item={showModal} setShowModal={setShowModal} />
                </Modal>
             }
            {
                itemSections.map(itemSection => (
                    !currentSection || currentSection === itemSection.id ? (<div key={itemSection.id}>
                        <h1>{itemSection.name}</h1>
                        <div className='item-section'>
                            {
                                itemSection.items.map(item => (
                                    <div key={item.id} className='item' onClick={() => setShowModal(item)}>
                                        <img src={item.picture} alt=''></img>
                                        <p>{item.name} - ${item.price}</p>
                                    </div>
                                ))
                            }
                        </div>
                    </div>) : null
                ))
            }
        </div>
    );
}

export default Items;
