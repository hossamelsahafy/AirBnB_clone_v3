#!/usr/bin/python3
"""State"""
from flask import Flask, jsonify, abort, request, Response
import json
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Get States"""
    states = [state.to_dict() for state in storage.all(State).values()]
    return Response(json.dumps(states, indent=4), mimetype='application/json')


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Get State ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return Response(json.dumps(state.to_dict(), indent=4),
                    mimetype='application/json')


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Delete OBJ"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Post State"""
    data = request.get__json(force=True, silent=True)
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**request.json)
    state.save()
    return Response(json.dumps(state.to_dict(), indent=4),
                    mimetype='application/json'), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    for key, value in request.json.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return Response(json.dumps(state.to_dict(), indent=4),
                    mimetype='application/json'), 200
