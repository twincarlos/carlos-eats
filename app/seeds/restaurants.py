from app.models import db, Restaurant


def seed_restaurants():
    starbucks = Restaurant(
        user_id=1,
        name="Starbucks",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/87641fb95384b3ab77577bd3cbf11195/c73ecc27d2a9eaa735b1ee95304ba588.jpeg",
        address="16305 Sw 88th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    mcdonalds = Restaurant(
        user_id=1,
        name="McDonald's",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/93211d08b3988b5acd81109a3229a43e/c73ecc27d2a9eaa735b1ee95304ba588.jpeg",
        address="15715 Sw 88th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    carvel = Restaurant(
        user_id=1,
        name="Carvel",
        picture="https://d1ralsognjng37.cloudfront.net/af053ed4-0cdd-421e-bfdc-662e99744385.jpeg",
        address="13071 SW 88th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    papa_johns = Restaurant(
        user_id=1,
        name="Papa Johns",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/21640e3d0b37907a2f79dfdca3785819/c73ecc27d2a9eaa735b1ee95304ba588.jpeg",
        address="15900 Sw 137th Ave",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    
    macondo_coffee = Restaurant(
        user_id=1,
        name="Macondo Coffee Roasters",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/552956472a70c3e0472ce01f80b99248/445a4b2618e10f7db95d4f17a85b117d.jpeg",
        address="13021 Sw 88th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    chick_fil_a = Restaurant(
        user_id=1,
        name="Chick-fil-A",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/8bb50af74218c79c9d1302f89bd7b670/445a4b2618e10f7db95d4f17a85b117d.jpeg",
        address="12100 Sw 88th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    cold_stone = Restaurant(
        user_id=1,
        name="Cold Stone Creamery",
        picture="https://d1ralsognjng37.cloudfront.net/213f8cf0-1725-4c3e-8af3-14547cf3b633",
        address="13624 Sw 88th St",
        latitude=123.45,
        longitude=123.45,
        horus=18
    )
    blaze_pizza = Restaurant(
        user_id=1,
        name="Blaze Pizza",
        picture="https://d1ralsognjng37.cloudfront.net/37369e27-6309-4466-a25a-006779fb0c9d.webp",
        address="12305 Sw 137th Ave",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )

    db.session.add(starbucks)
    db.session.add(mcdonalds)
    db.session.add(carvel)
    db.session.add(papa_johns)
    
    db.session.add(macondo_coffee)
    db.session.add(chick_fil_a)
    db.session.add(cold_stone)
    db.session.add(blaze_pizza)

    db.session.commit()

def undo_restaurants():
    db.session.execute('TRUNCATE restaurants RESTART IDENTITY CASCADE;')
    db.session.commit()
