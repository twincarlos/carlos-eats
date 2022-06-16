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
        hours=18
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

    juan_valdez = Restaurant(
        user_id=1,
        name="Juan Valdez Cafe",
        picture="https://d1ralsognjng37.cloudfront.net/3c63daf4-446e-4054-ab6c-58d018269c65.jpeg",
        address="3530 Nw 83rd Ave",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    wendys = Restaurant(
        user_id=1,
        name="Wendy's",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/749da7492d625ec1f24594c83f9863b0/c73ecc27d2a9eaa735b1ee95304ba588.jpeg",
        address="16203 Sw 88th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    lick_nitrogen = Restaurant(
        user_id=1,
        name="Lick Nitrogen Ice Cream",
        picture="https://duyt4h9nfnj50.cloudfront.net/resized/1539874673846-w1080-f3.jpg",
        address="2601 Sw 147th Ave",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    mod_pizza = Restaurant(
        user_id=1,
        name="MOD Pizza",
        picture="https://d1ralsognjng37.cloudfront.net/90aec12b-a59e-4eaf-a1b3-6642b81a079e.jpeg",
        address="8525 Mills Dr",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )

    dunkin_donuts = Restaurant(
        user_id=1,
        name="Dunkin' Donuts",
        picture="https://d1ralsognjng37.cloudfront.net/f2211e35-5e6b-4f33-a351-470f644fc483.jpeg",
        address="11790 Sw 88th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    taco_bell = Restaurant(
        user_id=1,
        name="Taco Bell",
        picture="https://d1ralsognjng37.cloudfront.net/d37e4be2-1ea7-40f0-90c6-4404aa5a9657.jpeg",
        address="15201 SW 104 St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    ice_cream_shop = Restaurant(
        user_id=1,
        name="The Ice Cream Shop",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/c2767c10d76b1ac0efbcb60d6327b384/ffd640b0f9bc72838f2ebbee501a5d4b.jpeg",
        address="12335 Sw 112th St",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    ragazza_pizza = Restaurant(
        user_id=1,
        name="Ragazza Pizza",
        picture="https://tb-static.uber.com/prod/image-proc/processed_images/381b2cf5811a82cf205e0089914103a3/289197f4b252306213575a01442f7b66.webp",
        address="2600 West Flavor St",
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

    db.session.add(juan_valdez)
    db.session.add(wendys)
    db.session.add(lick_nitrogen)
    db.session.add(mod_pizza)

    db.session.add(dunkin_donuts)
    db.session.add(taco_bell)
    db.session.add(ice_cream_shop)
    db.session.add(ragazza_pizza)

    db.session.commit()

def undo_restaurants():
    db.session.execute('TRUNCATE restaurants RESTART IDENTITY CASCADE;')
    db.session.commit()
