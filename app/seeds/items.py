from app.models import db, Item


def seed_items():
    # STARBUCKS
    # hot coffee
    caffe_americano = Item(
        menu_section_id=1,
        name="Caffe Americano",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8zNmZhNzQwZi03NGNlLTQyNWMtYTRlNy05Njg3NGU5MTZlNDYuanBlZw==",
        description="lorem ipsum",
        price=3.15
    )
    cappuccino = Item(
        menu_section_id=1,
        name="Capuccino",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC80YmE5ZjY2Zi0zZTdiLTRlZWItODJkYS1kNTRjNGFlOTk3MDUuanBlZw==",
        description="lorem ipsum",
        price=4.25
    )
    espresso_macchiato = Item(
        menu_section_id=1,
        name="Espresso Macchiato",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9kYzBmZDZhZi0wMzRkLTQzZGEtYjM1Ny1hZWY1Nzk5ZDM1NTQuanBlZw==",
        description="lorem ipsum",
        price=2.90
    )

    # MCDONALDS
    # combo meals
    crispy_chicken_sandwich = Item(
        menu_section_id=4,
        name="Crispy Chicken Sandwich Meal",
        picture="https://d1ralsognjng37.cloudfront.net/332fa8ec-f645-4032-b858-59cd78f241ef.jpeg",
        description="lorem ipsum",
        price=9.09
    )
    big_mac = Item(
        menu_section_id=4,
        name="Big Mac Meal",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/b9eb19b19727cbea4de310a92374e222/859baff1d76042a45e319d1de80aec7a.jpeg",
        description="lorem ipsum",
        price=9.99
    )
    chicken_nuggets = Item(
        menu_section_id=4,
        name="10 Piece McNuggets Meal",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/71ead9db896ec112fd16e0dfa247efe9/859baff1d76042a45e319d1de80aec7a.jpeg",
        description="lorem ipsum",
        price=9.99
    )

    db.session.add(caffe_americano)
    db.session.add(cappuccino)
    db.session.add(espresso_macchiato)
    db.session.add(crispy_chicken_sandwich)
    db.session.add(big_mac)
    db.session.add(chicken_nuggets)

    db.session.commit()

def undo_items():
    db.session.execute('TRUNCATE items RESTART IDENTITY CASCADE;')
    db.session.commit()
