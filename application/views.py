from application import application
from flask import render_template, request
from data import get_users_by_age, get_users_by_loc, get_users_by_id

@application.errorhandler(404)
def not_found(error):
  return render_template('404.html', title="Page Not Found")

@application.route('/view/users/user/<uid>')
def view_users_by_id(uid):
  user = get_users_by_id(uid)
  return render_template('users.html', 
                          users=[user],
                          title="Users By ID")

@application.route('/view/users/age')
def view_users_by_age():
  min_age = request.args.get('min_age')
  max_age = request.args.get('max_age')
  users_in_age_range = get_users_by_age(min_age, max_age)
  return render_template('users.html', 
                          users=users_in_age_range,
                          title="Users By Age")

@application.route('/view/users/loc')
def view_users_by_loc():
  lat = request.args.get('lat') 
  lon = request.args.get('long')
  dist = request.args.get('dist', 5) #defaults to 5
  users_in_distance = get_users_by_loc(lat, lon, dist)
  return render_template('map.html',
                          users=users_in_distance,
                          lat=lat, lon=lon, dist=dist,
                          title="Users By Location")

