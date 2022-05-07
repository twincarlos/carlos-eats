from flask_sqlalchemy import SQLAlchemy
from .db import db


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    menu_section_id = db.Column(db.Integer, db.ForeignKey("menu_sections.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)

    menu_section = db.relationship("Menu_Section", back_populates="items")
    cart_item = db.relationship("Cart_Item", back_populates="item", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "menu_section_id": self.menu_section_id,
            "name": self.name,
            "picture": self.picture,
            "description": self.description,
            "price": self.price
        }
