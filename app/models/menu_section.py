from flask_sqlalchemy import SQLAlchemy
from .db import db


class Menu_Section(db.Model):
    __tablename__ = "menu_sections"

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    name = db.Column(db.String, nullable=False)

    restaurant = db.relationship("Restaurant", back_populates="menu_sections")
    items = db.relationship("Item", back_populates="menu_section", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "restaurant_id": self.restaurant_id,
            "name": self.name,
            "items": [item.to_dict() for item in self.items]
        }
