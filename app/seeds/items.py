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
