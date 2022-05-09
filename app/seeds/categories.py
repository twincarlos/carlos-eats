from app.models import db, Category


def seed_categories():
    fast_food = Category(name="Fast Food")
    coffee = Category(name="Coffee")
    ice_cream = Category(name="Ice Cream")

    db.session.add(fast_food)
    db.session.add(coffee)
    db.session.add(ice_cream)

    db.session.commit()

def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()
