from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_picture = db.Column(db.String, nullable=False)

    restaurants = db.relationship("Restaurant", back_populates="user", cascade="all, delete")
    addresses = db.relationship("Address", back_populates="user", cascade="all, delete")
    favorites = db.relationship("Favorite", back_populates="user", cascade="all, delete")
    cart = db.relationship("Cart", back_populates="user", cascade="all, delete")
    orders = db.relationship("Order", back_populates="user", cascade="all, delete")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "profile_picture": self.profile_picture,
            "restaurants": [restaurant.to_dict() for restaurant in self.restaurants],
            "addresses": [address.to_dict() for address in self.addresses],
            "favorites": [favorite.to_dict() for favorite in self.favorites],
            "cart": self.cart.to_dict(),
            "orders": [order.to_dict() for order in self.orders]
        }