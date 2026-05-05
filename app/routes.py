from flask import Blueprint, jsonify
from .utils import add_numbers

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to Jenkins CI/CD Demo"})

@main.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = add_numbers(a, b)
    return jsonify({"result": result})