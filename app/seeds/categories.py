from app.models import db, Category


def seed_categories():
    fast_food = Category(name="Fast Food", picture="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/fastfood.png")
    coffee = Category(name="Coffee", picture="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/coffeeandtea.png")
    ice_cream = Category(name="Ice Cream", picture="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/icecreamandyogort.png")

    db.session.add(fast_food)
    db.session.add(coffee)
    db.session.add(ice_cream)

    db.session.commit()

def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()
