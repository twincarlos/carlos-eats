import './Restaurant.css';

function Items ({ itemSections, currentSection }) {
    return (
        <div id='items'>
            {
                itemSections.map(itemSection => (
                    !currentSection || currentSection === itemSection.id ? (<div key={itemSection.id}>
                        <p>{itemSection.name}</p>
                        <div className='item-section'>
                            {
                                itemSection.items.map(item => (
                                    <div key={item.id} className='item'>
                                        <img src={item.picture} alt=''></img>
                                        <p>{item.name}</p>
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
