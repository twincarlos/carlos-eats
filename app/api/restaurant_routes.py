from flask import Blueprint, request
from app.models import Restaurant, Category, Category_Detail, Favorite, db
from flask_login import current_user
import json

restaurant_routes = Blueprint("restaurants", __name__)

@restaurant_routes.route("", methods=["GET", "POST"])
def all_restaurants():
    if request.method == "GET":
        all_categories = Category_Detail.query.all()
        categories = []

        for category in all_categories:
            categories.append(category.to_dict())

        return { "categories": categories }

@restaurant_routes.route("/<int:restaurant_id>", methods=["GET", "PUT", "DELETE"])
def one_restaurant(restaurant_id):
    if request.method == "GET":
        return Restaurant.query.get(restaurant_id).to_dict()

@restaurant_routes.route("/search/<string:keyword>", methods=["GET"])
def search_restaurants(keyword):
    if request.method == "GET":
        restaurants = Restaurant.query.filter(Restaurant.name.ilike(f"%{keyword}%"))
        return { 'restaurants': [restaurant.to_dict() for restaurant in restaurants] }

@restaurant_routes.route("/favorite/<int:restaurant_id>", methods=["POST", "DELETE"])
def favorite_restaurant(restaurant_id):
    if request.method == "POST":
        favorited_restaurant = Favorite(user_id=current_user.id, restaurant_id=restaurant_id)
        db.session.add(favorited_restaurant)
        db.session.commit()
        return favorited_restaurant.to_dict()
    if request.method == "DELETE":
        unfavorited_restaurant = Favorite.query.filter(Favorite.user_id == current_user.id, Favorite.restaurant_id == restaurant_id).first()
        db.session.delete(unfavorited_restaurant)
        db.session.commit()
        return str(restaurant_id)
