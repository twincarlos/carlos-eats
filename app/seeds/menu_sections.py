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
    shakes = Menu_Section(restaurant_id=3, name="Shakes")
    dessert_packs = Menu_Section(restaurant_id=3, name="Dessert Packs")

    db.session.add(hot_coffees)
    db.session.add(cold_coffees)
    db.session.add(bakery)
    db.session.add(combo_meals)
    db.session.add(shareables)
    db.session.add(beverages)
    db.session.add(sundaes)
    db.session.add(shakes)
    db.session.add(dessert_packs)

    db.session.commit()

def undo_menu_sections():
    db.session.execute('TRUNCATE menu_sections RESTART IDENTITY CASCADE;')
    db.session.commit()
