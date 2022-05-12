import './Restaurant.css';

function ItemSections ({ itemSections, setCurrentSection }) {
    return (
        <div id='menu-sections'>
            <p onClick={() => setCurrentSection(null)}>All items</p>
            {
                itemSections.map(itemSection => <p onClick={() => setCurrentSection(itemSection.id)} key={itemSection.id}>{itemSection.name}</p>)
            }
        </div>
    );
}

export default ItemSections;
