from flask import Blueprint, request
from app.models import Restaurant, Category, Category_Detail, db
import json

restaurant_routes = Blueprint("restaurants", __name__)

@restaurant_routes.route("", methods=["GET", "POST"])
def all_restaurants():
    if request.method == "GET":
        all_categories = Category.query.all()
        categories = []

        for category in all_categories:
            category_detail = Category_Detail.query.filter(Category_Detail.category_id == category.id).first()
            categories.append(category_detail.to_dict())

        return { "categories": categories }

@restaurant_routes.route("/<int:restaurant_id>", methods=["GET", "PUT", "DELETE"])
def one_restaurant(restaurant_id):
    if request.method == "GET":
        return Restaurant.query.get(restaurant_id).to_dict()
