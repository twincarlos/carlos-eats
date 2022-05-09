from app.models import db, Restaurant


def seed_restaurants():
    starbucks = Restaurant(
        user_id=1,
        name="Starbucks",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvY2YzNzdiZGU1NTMxOThjZGQ0MmNkNjkxY2VlMDRjNzcvODIwODgzYTQ4NTY3NjcwYWNiZDcyMGJjNzYzOTEyOTEuanBlZw==",
        address="lorem ipsum",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    mcdonalds = Restaurant(
        user_id=1,
        name="McDonald's",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC9pbWFnZS1wcm9jL3Byb2Nlc3NlZF9pbWFnZXMvOTMyMTFkMDhiMzk4OGI1YWNkODExMDlhMzIyOWE0M2UvODIwODgzYTQ4NTY3NjcwYWNiZDcyMGJjNzYzOTEyOTEuanBlZw==",
        address="lorem ipsum",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )
    carvel = Restaurant(
        user_id=1,
        name="Carvel",
        picture="https://cn-geo1.uber.com/image-proc/resize/eats/format=webp/width=550/height=440/quality=70/srcb64=aHR0cHM6Ly9kMXJhbHNvZ25qbmczNy5jbG91ZGZyb250Lm5ldC8xYzliZWMzNS1mNGE5LTQ0MWItYTIzYi1jYzJmOTkyNmEzOGEuanBlZw==",
        address="lorem ipsum",
        latitude=123.45,
        longitude=123.45,
        hours=18
    )

    db.session.add(starbucks)
    db.session.add(mcdonalds)
    db.session.add(carvel)

    db.session.commit()

def undo_restaurants():
    db.session.execute('TRUNCATE restaurants RESTART IDENTITY CASCADE;')
    db.session.commit()
