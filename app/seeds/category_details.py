from app.models import db, Category_Detail


def seed_category_details():
    starbucks_coffee = Category_Detail(category_id=1, restaurant_id=1)
    mcdonalds_fast_food = Category_Detail(category_id=2, restaurant_id=2)
    carvel_ice_cream = Category_Detail(category_id=3, restaurant_id=3)
    papa_johns_pizza = Category_Detail(category_id=4, restaurant_id=4)
    
    macondo_coffee = Category_Detail(category_id=1, restaurant_id=5)
    chick_fil_a_fast_food = Category_Detail(category_id=2, restaurant_id=6)
    cold_stone_ice_cream = Category_Detail(category_id=3, restaurant_id=7)
    blaze_pizza = Category_Detail(category_id=4, restaurant_id=8)
    
    juan_valdez_coffee = Category_Detail(category_id=1, restaurant_id=9)
    wendys_fast_food = Category_Detail(category_id=2, restaurant_id=10)
    nitrogen_ice_cream = Category_Detail(category_id=3, restaurant_id=11)
    mod_pizza = Category_Detail(category_id=4, restaurant_id=12)

    db.session.add(starbucks_coffee)
    db.session.add(mcdonalds_fast_food)
    db.session.add(carvel_ice_cream)
    db.session.add(papa_johns_pizza)
    
    db.session.add(macondo_coffee)
    db.session.add(chick_fil_a_fast_food)
    db.session.add(cold_stone_ice_cream)
    db.session.add(blaze_pizza)
    
    db.session.add(juan_valdez_coffee)
    db.session.add(wendys_fast_food)
    db.session.add(nitrogen_ice_cream)
    db.session.add(mod_pizza)

    db.session.commit()

def undo_category_details():
    db.session.execute('TRUNCATE category_details RESTART IDENTITY CASCADE;')
    db.session.commit()
