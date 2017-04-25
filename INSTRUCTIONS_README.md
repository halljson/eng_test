Jason Hall
ICXMedia - Engineering Test

------------------------------------------------------------------------------

This application is implemented with Python 2.7.10. If you have other 
versions of python on your machine, please see the following link before 
making a virtual environment for this application: 
http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv

All virtual environment commands are shown with virtualenvwrapper commands.
https://virtualenvwrapper.readthedocs.io/en/latest/
$ pip install virtualenvwrapper


------------------------------------------------------------------------------
------------------------------------------------------------------------------


Running the application:

cd to the top level of the repo
$ mkvirtualenv <envname>          (reactivate this later w/ $workon <envname>)
$ pip install -r requirements.txt
$ python application.py

------------------------------------------------------------------------------

Check out the following links:

Basic Backend Funcionality (ingesting csv, returning JSON)
http://localhost:5000/users/user/1
http://localhost:5000/users/loc?lat=38.900918&long=-77.035857
http://localhost:5000/users/age?min_age=21&max_age=32

Basic Frontend Functionality (ingesting csv, displaying html table)
simply add '/view' in front of any of the above links:
http://localhost:5000/view/users/user/1
http://localhost:5000/view/users/age?min_age=21&max_age=32

------------------------------------------------------------------------------

Bonus round!

Map display: 
http://localhost:5000/view/users/loc?lat=38.900918&long=-77.035857

Custom distance queries (units in mi): 
http://localhost:5000/view/users/loc?lat=38.900918&long=-77.035857&dist=35
http://localhost:5000/view/users/loc?lat=38.900918&long=-77.035857&dist=55

------------------------------------------------------------------------------

When you're done running the python application, kill it with 'ctrl-c' into 
the terminal and then exit the virtual environment with:
$ deactivate


------------------------------------------------------------------------------
------------------------------------------------------------------------------


                     Things I like about my implementation:
                             (other than the favicon)

I think the custom distance query is fun to play with. Adding a distance 
slider would be pretty cool, but would require more work done in the JS or 
constant GET requests.  

Clicking any pin on the map reveals that person's full name and username.

I wanted to use a mysql database but I think it would have been a little 
overkill. Instead, I kept the access to the csv file local to data.py (where 
that information is used), so I could easily yank out that code to make the 
system work with any db without having to change much (any?) code elsewhere.


My get_users_by_loc() method cleaned up beautifully:

def get_users_by_loc(lat, lon):
  coords = (d(lat), d(lon))
  users_in_distance = []
  for user in users:
    user_loc = (d(user['lat']), d(user['long']))
    if distance.vincenty(coords, user_loc) < 5:
      users_in_distance += [user]
  return users_in_distance

...went to...

def get_users_by_loc(lat, lon, dist):
  return [user for user in users if miles_between(coords, user) < int(dist)]

And two other one-line helpers...

:thumbsup:

------------------------------------------------------------------------------

                   Things I don't like about my implementation:

I should have broken up the final commit into many, many more git commits.

My views aren't completely disconnected from the backend, rather, they call 
the same methods that my api does - they get JSON back from these methods and 
then the template tells the web framework how to render this information for 
the user.

The reason I didn't use ajax is because I'm not perfectly familiar with  
asynchronous calls from the front-end side of things. (You can see I used xhr 
for a synchronous request in the inline Javascript in the map.html file, 
thankfully we're only processing 101 entities). 

The endpoint /users/user/<int> returns a json list with only a single entry, 
this probably shouldn't be a list, but making it return a list made the 
front-end table template (users.html) one-size-fits-all with only two 
brackets in the views.py file (line 13).

Unnecessarily large folder structure - here I intentionally left empty 
directories in place to show I know how I would organize more than just 
what's included here!

I could have warned the user when they input a bad query, like min_age being 
greater than max_age.

I could have gone further with adding RESTful post and delete capabilities
but am a little too pressed for time to spin up the parsers and mysql db! 
Though, you really ought to see how Flask handles this kind of thing - I once
used MySqlAlchemy alongside Flask-Restful (two Python modules that play well 
with Flask) for some awesome code to handle all this!
