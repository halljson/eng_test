from csv import DictReader
from decimal import Decimal as d
from geopy.distance import vincenty as distance_between

# Ingest CSV into Dict with named key/value pairs
with open('user.csv') as f: 
  users = [{k: str(v) for k, v in row.items()} for row in DictReader(f, skipinitialspace=True)]

# users[i] now looks like:
# {'age': '45',
#  'comments': '23',
#  'dislikes': '300',
#  'fname': 'John',
#  'gender': 'male',
#  'id': '1',
#  'lat': '38.900918',
#  'likes': '10',
#  'lname': 'Doe',
#  'long': '-77.035857',
#  'retweets': '35',
#  'username': 'jdoe'}

def get_users_by_id(uid):
  uid = int(uid)
  if uid > len(users) or uid <= 0:
    return None
  return users[uid-1]

def get_users_by_age(min_age, max_age):
  min_age = int(min_age)
  max_age = int(max_age)
  if min_age > max_age: return []
  # users_in_age_range = []
  # if min_age < max_age:
    # users_in_age_range = 
  # return users_in_age_range
  return [user for user in users if int(user['age']) in range(min_age, max_age)]

# Helper method for get_users_by_loc
# Takes a user, returns location as tuple
def user_coords(user): 
  return (d(user['lat']), d(user['long']))

# Helper method for get_users_by_loc
def miles_between(coords, user):
  return distance_between(coords, user_coords(user)).miles

def get_users_by_loc(lat, lon, dist):
  coords = (d(lat), d(lon)) 
  return [user for user in users if miles_between(coords, user) < int(dist)]

