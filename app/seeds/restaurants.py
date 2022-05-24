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

    db.session.add(starbucks)
    db.session.add(mcdonalds)
    db.session.add(carvel)
    db.session.add(papa_johns)

    db.session.commit()

def undo_restaurants():
    db.session.execute('TRUNCATE restaurants RESTART IDENTITY CASCADE;')
    db.session.commit()
