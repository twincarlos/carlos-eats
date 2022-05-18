from flask_sqlalchemy import SQLAlchemy
from .db import db


class Cart_Item(db.Model):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    cart = db.relationship("Cart", back_populates="cart_items")
    item = db.relationship("Item", back_populates="cart_item")

    def to_dict(self):
        return {
            "id": self.id,
            "cart_id": self.cart_id,
            "item": self.item.to_dict(),
            "quantity": self.quantity
        }
