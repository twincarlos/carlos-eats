from app.models import db, Item


def seed_items():
    # STARBUCKS
    # hot coffees
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
    # cold coffees
    cold_brew = Item(
        menu_section_id=2,
        name="Cold Brew Coffee with Milk",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC84ZTBlMmZmMy0yYzVlLTQzYWItOGY4YS05M2ViNTE0OTY1ZDcuanBlZw==",
        description="lorem ipsum",
        price=4.55
    )
    salted_caramel = Item(
        menu_section_id=2,
        name="Salted Caramel Cream Cold Brew",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9kMzAxN2Q3Ny05MTk0LTQ2ZDItYjQ0Zi01Zjk1ZGFmODAyZjMuanBlZw==",
        description="lorem ipsum",
        price=5.45
    )
    iced_white_chocolate = Item(
        menu_section_id=2,
        name="Iced White Chocolate Mocha",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9hNWJkYTc4Ny0zMjZiLTRlYTYtODc1YS04YmM4ZDc2MTRmYjEuanBlZw==",
        description="lorem ipsum",
        price=5.75
    )
    #bakery
    everything_bagel = Item(
        menu_section_id=3,
        name="Everything Bagel",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC85ZWM0MjdmMy1kNmIxLTRiNzYtYmE3MC0xOTcwNGY3OWM1M2YuanBlZw==",
        description="lorem ipsum",
        price=2.65
    )
    butter_croissant = Item(
        menu_section_id=3,
        name="Butter Croissant",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC80ZGMyOGRkNC1hMDYzLTRkYWItYmNhZi1lZTc1ZWJiZjZiZGYuanBlZw==",
        description="lorem ipsum",
        price=3.75
    )
    unicorn_cake_pop = Item(
        menu_section_id=3,
        name="Unicorn Cake Pop",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvZTkwZmM1ZjMyOTM3NTIwMjRhZmFmYzBjNzI1NDQ3NzAvODU5YmFmZjFkNzYwNDJhNDVlMzE5ZDFkZTgwYWVjN2EuanBlZw==",
        description="lorem ipsum",
        price=3.45
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
    # shareables
    mcnuggets_40 = Item(
        menu_section_id=5,
        name="40 McNuggets",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9hMjYzMjQ2MS1kZGVkLTQwNmQtYWM2Zi1lM2UyNjk5ODEzNTcuanBlZw==",
        description="lorem ipsum",
        price=14.99
    )
    large_fries_2 = Item(
        menu_section_id=5,
        name="2 Large Fries",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9jMjM2ODMyNC02ODk2LTRhODQtYjYxOS1jMTA2YmFlOGFmNGEuanBlZw==",
        description="lorem ipsum",
        price=7.89
    )
    cookie_tote_13 = Item(
        menu_section_id=5,
        name="13 Cookie Tote",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8yNGIzMjM0OS0xMTQ5LTQzODAtYThjOC01ZjJhZDViM2Y2NWQuanBlZw==",
        description="lorem ipsum",
        price=8.09
    )
    # beverages
    medium_coke = Item(
        menu_section_id=6,
        name="Medium Coke",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvYjBlOWQzY2JjZDZhMDcwZTc2N2Q5M2IzYzRjZjU4Y2MvODU5YmFmZjFkNzYwNDJhNDVlMzE5ZDFkZTgwYWVjN2EuanBlZw==",
        description="lorem ipsum",
        price=1.89
    )
    water = Item(
        menu_section_id=6,
        name="Dasani Bottled Water",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8wZTUzYTE0ZS1mZGE0LTQ3MWItOGRhYS05MzA3YjQ2NDkzOTEuanBlZw==",
        description="lorem ipsum",
        price=2.69
    )
    slushie = Item(
        menu_section_id=6,
        name="Medium Minute Maid Strawberry Watermelon Slushie",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvZjcwYTExYjIyZWFlMzhiZGY1YTk3YzZkYWQzZjZiN2MvODU5YmFmZjFkNzYwNDJhNDVlMzE5ZDFkZTgwYWVjN2EuanBlZw==",
        description="lorem ipsum",
        price=3.49
    )

    # CARVEL
    # sundaes
    ice_cream_sundae = Item(
        menu_section_id=7,
        name="Ice Cream Sundae",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9kN2I3YjZhNi0yZjhkLTQyMzMtODY3Ny01NzI5MGFjMTJlZGUuanBlZw==",
        description="lorem ipsum",
        price=4.99
    )
    cup_of_toppings = Item(
        menu_section_id=7,
        name="Cup of Toppings",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC80Y2RiZDhmOS1kMjJhLTRmZDItYjdjZC1lYzUyYTljYzI5MmQuanBlZw==",
        description="lorem ipsum",
        price=2.99
    )
    bananas_sundae = Item(
        menu_section_id=7,
        name="Bananas Foster Sundae Dasher",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8zNDM1YTJhMi0yOWMzLTQzMjEtYjFkYS1lZTljZGU5YTE1OTAuanBlZw==",
        description="lorem ipsum",
        price=5.29
    )
    # ice creams
    soft_ice_cream = Item(
        menu_section_id=8,
        name="Soft Serve Ice Cream",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9hYzk5ZTU2Yy00YTEwLTQzZmMtOTlhMS1jNThmMzk0NzkzZDIuanBlZw==",
        description="lorem ipsum",
        price=2.99
    )
    scooped_ice_cream = Item(
        menu_section_id=8,
        name="Scooped Ice Cream",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9iZmMxYmNlOC0zNjc2LTRmODItYTQ0YS05OTI3YTg4Y2FhNjUuanBlZw==",
        description="lorem ipsum",
        price=2.99
    )
    sorbet_scooped = Item(
        menu_section_id=8,
        name="Sorbet Scooped",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC84OWUxY2ExYy0wNDdlLTQzN2QtODQ1Ni0yOGZiMGQ5ODU5ZjEuanBlZw==",
        description="lorem ipsum",
        price=2.99
    )
    # dessert packs
    flying_saucers = Item(
        menu_section_id=9,
        name="Flying Saucers (6-Pack)",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9iMzYxNjU5Ni00Y2RmLTQ3OTktYTFkMy05ODRkY2YxMjNhMWYuanBlZw==",
        description="lorem ipsum",
        price=7.99
    )
    deluxe_flying_saucers = Item(
        menu_section_id=9,
        name="Deluxe Flying Saucers (6-Pack)",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8xZTBlNWJjOC1iOTQ0LTRhMDAtYmY5Yy1kODY2NmZiYjM0MGIuanBlZw==",
        description="lorem ipsum",
        price=9.99
    )
    oreo_rounders = Item(
        menu_section_id=9,
        name="Oreo Rounders (6-Pack)",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8wMjQxNWQ5MS1lOGFmLTRlZTUtOGJjNy00MTgwNTkxZjcxMGMuanBlZw==",
        description="lorem ipsum",
        price=9.99
    )

    # PAPA JOHNS
    # pizza
    cheesy_alfredo = Item(
        menu_section_id=10,
        name="Extra Cheesy Alfredo",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvODBkMDA2YjU2Y2YwYTlmZWJiYjYyZTM5ZDk2ZGYyY2UvODU5YmFmZjFkNzYwNDJhNDVlMzE5ZDFkZTgwYWVjN2EuanBlZw==",
        description="lorem ipsum",
        price=14.00
    )
    pepperoni = Item(
        menu_section_id=10,
        name="Pepperoni",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvNzU5ZGU1YmZiZmQ4ZmU3MGNmYTZmZmJmYWFiMjBjMTIvODU5YmFmZjFkNzYwNDJhNDVlMzE5ZDFkZTgwYWVjN2EuanBlZw==",
        description="lorem ipsum",
        price=12.50
    )
    garden_fresh = Item(
        menu_section_id=10,
        name="Garden Fresh",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvNTM0ZWMxYmMzMGU2MDVmODUzZjVmOTk4ZjlhZmZiMGMvODU5YmFmZjFkNzYwNDJhNDVlMzE5ZDFkZTgwYWVjN2EuanBlZw==",
        description="lorem ipsum",
        price=14.00
    )
    # papadias
    parmesan_papadias = Item(
        menu_section_id=11,
        name="Parmesan Crusted Papadias",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC80MzhlMTkwNS1iYjk5LTRhNDEtOGYxMi02MzgxYzA4NzQxNTguanBlZw==",
        description="lorem ipsum",
        price=9.00
    )
    papadias = Item(
        menu_section_id=11,
        name="Papadias",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9kODZiNDAxNC02N2Q0LTQ5OTgtOWVhMi04YTRhOGYxZjczYmIuanBlZw==",
        description="lorem ipsum",
        price=8.00
    )
    # sides
    rolls = Item(
        menu_section_id=12,
        name="Rolls",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC9iMTgyMGJhYi1mMjFiLTQ5YzEtODZkYS1kMDhhZDBlMTk4YTcuanBlZw==",
        description="lorem ipsum",
        price=7.00
    )
    chicken_wings = Item(
        menu_section_id=12,
        name="Chicken Wings",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvM2EzNzcyMWE3NDZhZGZmYWZmOTEzMmM4Y2IzZDU5ZTUvODU5YmFmZjFkNzYwNDJhNDVlMzE5ZDFkZTgwYWVjN2EuanBlZw==",
        description="lorem ipsum",
        price=9.00
    )
    knots = Item(
        menu_section_id=12,
        name="Knots",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8zZjZlYTQwYy02Yjg2LTRiZTQtYmU0Zi00YzA1Njg3NjE1OWQuanBlZw==",
        description="lorem ipsum",
        price=7.00
    )

    db.session.add(caffe_americano)
    db.session.add(cappuccino)
    db.session.add(espresso_macchiato)
    db.session.add(cold_brew)
    db.session.add(salted_caramel)
    db.session.add(iced_white_chocolate)
    db.session.add(everything_bagel)
    db.session.add(butter_croissant)
    db.session.add(unicorn_cake_pop)

    db.session.add(crispy_chicken_sandwich)
    db.session.add(big_mac)
    db.session.add(chicken_nuggets)
    db.session.add(mcnuggets_40)
    db.session.add(large_fries_2)
    db.session.add(cookie_tote_13)
    db.session.add(medium_coke)
    db.session.add(water)
    db.session.add(slushie)

    db.session.add(ice_cream_sundae)
    db.session.add(cup_of_toppings)
    db.session.add(bananas_sundae)
    db.session.add(soft_ice_cream)
    db.session.add(scooped_ice_cream)
    db.session.add(sorbet_scooped)
    db.session.add(flying_saucers)
    db.session.add(deluxe_flying_saucers)
    db.session.add(oreo_rounders)

    db.session.add(cheesy_alfredo)
    db.session.add(pepperoni)
    db.session.add(garden_fresh)
    db.session.add(parmesan_papadias)
    db.session.add(papadias)
    db.session.add(rolls)
    db.session.add(chicken_wings)
    db.session.add(knots)

    db.session.commit()

def undo_items():
    db.session.execute('TRUNCATE items RESTART IDENTITY CASCADE;')
    db.session.commit()
