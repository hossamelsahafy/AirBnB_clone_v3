#!/usr/bin/python3
"""Cities"""
from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """Get cities"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    all_cities = []
    for city in state.cities:
        all_cities.append(city.to_dict())
    return jsonify(all_cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Get city Id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Delete City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """Create City"""
    data = request.get_json(force=True, silent=True)
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    new_city = City(**data)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Update City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'state_id']:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
