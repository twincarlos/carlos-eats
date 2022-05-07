from flask_sqlalchemy import SQLAlchemy
from .db import db


class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)

    user = db.relationship("User", back_populates="cart")
    restaurant = db.relationship("Restaurant", back_populates="carts")
    cart_items = db.relationship("Cart_Item", back_populates="cart", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "restaurant": self.restaurant,
            "cart_items": [cart_item.to_dict() for cart_item in self.cart_items]
        }
