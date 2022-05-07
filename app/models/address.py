from flask_sqlalchemy import SQLAlchemy
from .db import db


class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    address = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    user = db.relationship("User", back_populates="addresses")

    def to_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
