from app.models import db, Category_Detail


def seed_category_details():
    starbucks_coffee = Category_Detail(category_id=1, restaurant_id=1)
    mcdonalds_fast_food = Category_Detail(category_id=2, restaurant_id=2)
    carvel_ice_cream = Category_Detail(category_id=3, restaurant_id=3)
    papa_johns_pizza = Category_Detail(category_id=4, restaurant_id=4)

    db.session.add(starbucks_coffee)
    db.session.add(mcdonalds_fast_food)
    db.session.add(carvel_ice_cream)
    db.session.add(papa_johns_pizza)

    db.session.commit()

def undo_category_details():
    db.session.execute('TRUNCATE category_details RESTART IDENTITY CASCADE;')
    db.session.commit()
