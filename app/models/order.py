from flask_sqlalchemy import SQLAlchemy
from .db import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    restaurant_name = db.Column(db.String, nullable=False)
    restaurant_picture = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Float, nullable=False)

    user = db.relationship("User", back_populates="orders")
    order_items = db.relationship("Order_Item", back_populates="order", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "restaurant_name": self.restaurant_name,
            "restaurant_picture": self.restaurant_picture,
            "time": self.time,
            "total": self.total,
            "order_items": [order_item.to_dict() for order_item in self.order_items]
        }
