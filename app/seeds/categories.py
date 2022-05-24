from app.models import db, Category


def seed_categories():
    coffee = Category(name="Coffee", picture="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/coffeeandtea.png")
    fast_food = Category(name="Fast Food", picture="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/fastfood.png")
    ice_cream = Category(name="Ice Cream", picture="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/icecreamandyogort.png")
    pizza = Category(name="Pizza", picture="https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/pizza.png")

    db.session.add(coffee)
    db.session.add(fast_food)
    db.session.add(ice_cream)
    db.session.add(pizza)

    db.session.commit()

def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()
