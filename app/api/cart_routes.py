from flask import Blueprint, request
from app.models import Cart, Cart_Item, db
from flask_login import current_user
import json

cart_routes = Blueprint("carts", __name__)

@cart_routes.route("", methods=["POST"])
def create_cart():
    if request.method == "POST":
        data = request.json
        new_cart = Cart(user_id=current_user.id, restaurant_id=data["restaurant_id"])
        db.session.add(new_cart)
        db.session.commit()
        return new_cart.to_dict()

@cart_routes.route("/<int:cart_id>", methods=["GET", "DELETE"])
def one_cart(cart_id):
    cart = Cart.query.get(cart_id)

    if request.method == "GET":
        return cart.to_dict()

    if request.method == "DELETE":
        db.session.delete(cart)
        db.session.commit()
        return str(cart_id)

@cart_routes.route("/<int:cart_id>/add_cart_item", methods=["POST"])
def add_cart_item(cart_id):
    data = request.json

    if request.method == "POST":
        new_cart_item = Cart_Item(cart_id=cart_id, item_id=data["item_id"], quantity=data["quantity"])
        db.session.add(new_cart_item)
        db.session.commit()
        return new_cart_item.to_dict()

@cart_routes.route("<int:cart_id>/cart_item/<int:cart_item_id>", methods=["PUT", "DELETE"])
def one_cart_item(cart_id, cart_item_id):
    cart_item = Cart_Item.query.get(cart_item_id)
    data = request.json

    if request.method == "PUT":
        cart_item.quantity = data["quantity"]
        db.session.commit()
        return cart_item.to_dict()

    if request.method == "DELETE":
        db.session.delete(cart_item)
        db.session.commit()
        return str(cart_item_id)
