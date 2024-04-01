#!/usr/bin/python3
"""Places Reviews"""

from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews(place_id):
    """Get all reviews of a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    all_reviews = [review.to_dict() for review in place.reviews]
    return jsonify(all_reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Get a review by id"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Delete a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """Create a review"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    if 'text' not in data:
        abort(400, 'Missing text')
    user_id = data['user_id']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data['place_id'] = place_id
    new_review = Review(**data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201

# work pgaa ya koodsoomk


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
