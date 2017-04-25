from application import application
from decimal import Decimal as d
from flask import jsonify, request
from flask_restful import Resource, reqparse, marshal_with, fields, marshal
from data import get_users_by_age, get_users_by_loc, get_users_by_id

@application.route('/users/user/<uid>')
def request_users_by_id(uid):
  user = get_users_by_id(uid)
  return jsonify(user)

@application.route('/users/age')
def request_users_by_age():
  min_age = request.args.get('min_age')
  max_age = request.args.get('max_age')
  users_in_age_range = get_users_by_age(min_age, max_age)
  return jsonify(users_in_age_range)

@application.route('/users/loc')
def request_users_by_loc():
  lat = request.args.get('lat') 
  lon = request.args.get('long')
  dist = request.args.get('dist', 5) #defaults to 5
  users_in_distance = get_users_by_loc(lat, lon, dist)
  return jsonify(users_in_distance)

