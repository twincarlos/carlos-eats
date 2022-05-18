from flask import Blueprint, request
from app.models import Order, Order_Item, db
from flask_login import current_user
import json

order_routes = Blueprint("orders", __name__)

@order_routes.route("", methods=["POST"])
def create_order():
    if request.method == "POST":
        data = request.json

        new_order = Order(
            user_id=current_user.id,
            restaurant_name=data["restaurant_name"],
            restaurant_picture=data["restaurant_picture"],
            time=data["time"]
        )
        db.session.add(new_order)
        db.session.commit()

        for order_item in data["order_items"]:
            new_order_item = Order_Item(
                order_id=new_order.id,
                item_name=order_item["name"],
                item_price=order_item["price"],
                quantity=order_item["quantity"]
            )
            db.session.add(new_order_item)
            db.session.commit()

        return new_order.to_dict()
