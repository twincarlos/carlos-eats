from flask_sqlalchemy import SQLAlchemy
from .db import db


class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    picture = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    hours = db.Column(db.Integer)

    user = db.relationship("User", back_populates="restaurants")
    favorites = db.relationship("Favorite", back_populates="restaurant", cascade="all, delete")
    menu_sections = db.relationship("Menu_Section", back_populates="restaurant", cascade="all, delete")
    carts = db.relationship("Cart", back_populates="restaurant", cascade="all, delete")
    category_detail = db.relationship("Category_Detail", back_populates="restaurant", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "picture": self.picture,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "hours": self.hours,
            "menu_sections": [menu_section.to_dict() for menu_section in self.menu_sections]
        }
