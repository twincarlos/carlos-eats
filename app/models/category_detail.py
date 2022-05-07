from flask_sqlalchemy import SQLAlchemy
from .db import db


class Category_Detail(db.Model):
    __tablename__ = "category_details"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)

    category = db.relationship("Category", back_populates="category_detail")
    restaurant = db.relationship("Restaurant", back_populates="category_detail")

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "restaurant": self.restaurant
        }
