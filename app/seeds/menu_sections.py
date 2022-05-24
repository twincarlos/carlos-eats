from app.models import db, Menu_Section


def seed_menu_sections():
    # STARBUCKS
    hot_coffees = Menu_Section(restaurant_id=1, name="Hot Coffees")
    cold_coffees = Menu_Section(restaurant_id=1, name="Cold Coffees")
    bakery = Menu_Section(restaurant_id=1, name="Bakery")

    # MCDONALDS
    combo_meals = Menu_Section(restaurant_id=2, name="Combo Meals")
    shareables = Menu_Section(restaurant_id=2, name="Shareables")
    beverages = Menu_Section(restaurant_id=2, name="Beverages")

    # CARVEL
    sundaes = Menu_Section(restaurant_id=3, name="Sundaes")
    ice_creams = Menu_Section(restaurant_id=3, name="Ice Creams")
    dessert_packs = Menu_Section(restaurant_id=3, name="Dessert Packs")

    # PAPA JOHNS
    pizza = Menu_Section(restaurant_id=4, name="Pizza")
    papadias = Menu_Section(restaurant_id=4, name="Papadias")
    sides = Menu_Section(restaurant_id=4, name="Sides")

    db.session.add(hot_coffees)
    db.session.add(cold_coffees)
    db.session.add(bakery)

    db.session.add(combo_meals)
    db.session.add(shareables)
    db.session.add(beverages)

    db.session.add(sundaes)
    db.session.add(ice_creams)
    db.session.add(dessert_packs)

    db.session.add(pizza)
    db.session.add(papadias)
    db.session.add(sides)

    db.session.commit()

def undo_menu_sections():
    db.session.execute('TRUNCATE menu_sections RESTART IDENTITY CASCADE;')
    db.session.commit()
