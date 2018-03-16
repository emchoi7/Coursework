#Eugene Choi
import json
import cherrypy
from _movie_database import _movie_database

mdb = _movie_database()
mdb.load_movies('ml-1m/movies.dat')
mdb.load_users('ml-1m/users.dat')
mdb.load_ratings('ml-1m/ratings.dat')
mdb.load_images()

class MoviesController(object):

	def GET(self):
		output = {'result':'success'}
		entries = []

		for key in mdb.movies:
			try:
				entries.append({'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1], 'result':'success', 'img':mdb.images[key]})
			except KeyError as ex:
				entries.append({'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1], 'result':'success'})
		
		try:
			output['movies'] = entries
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST(self):#adding a new movie
		output = {'result':'success'}
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['title'])
		data.append(the_body['genres'])
		mid = max(mdb.movies.keys()) + 1 #generate new movie id
		output['id'] = mid
		try:
			mdb.movies[mid] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self):
		output = {"result":"success"}

		mdb.movies = {}

		return json.dumps(output)

class MIDController(object):

	def GET(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			if key in mdb.images:
				output = {'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1], 'img':mdb.images[key]}
			else:
				output = {'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1]}
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'

		return json.dumps(output)

	def PUT(self,key):
		output = {'result':'success'}
		key = int(key)
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['title'])
		data.append(the_body['genres'])

		try:
			mdb.movies[key] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			del mdb.movies[key]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)



class UserController(object):

	def GET(self):
		output = {'result':'success'}
		entries = []

		for key in mdb.users:
			entries.append({'id':key, 'gender':mdb.users[key][0], 'age':mdb.users[key][1], 'occupation':mdb.users[key][2], 'zipcode':mdb.users[key][3]})

		try:
			output['users'] = entries
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST(self): #add a new user
		output = {'result':'success'}
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['gender'])
		data.append(the_body['age'])
		data.append(the_body['occupation'])
		data.append(the_body['zipcode'])
		uid = max(mdb.users.keys()) + 1 #generate new user id
		output['id'] = uid
		try:
			mdb.users[uid] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self):
		output = {'result':'success'}

		mdb.users = {}

		return json.dumps(output)

class UIDController(object):

	def GET(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			output = {'id':key, 'gender':mdb.users[key][0], 'age':mdb.users[key][1], 'occupation':mdb.users[key][2], 'zipcode':mdb.users[key][3]}
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def PUT(self,key):
		output = {'result':'success'}
		key = int(key)
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['gender'])
		data.append(the_body['age'])
		data.append(the_body['occupation'])
		data.append(the_body['zipcode'])

		try:
			mdb.users[key] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			del mdb.users[key]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

class RecController(object):

	def DELETE(self):
		output = {'result':'success'}

		return json.dumps(output)

	def GET(self,key):
		output = {'result':'success'}
		key = int(key)
		rec = mdb.get_highest_unrated_movie(key)

		try:
			output['movie_id'] = rec
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def PUT(self,key):
		output = {'result':'success'}
		uid = int(key)
		the_body = json.loads(cherrypy.request.body.read())
		mid = int(the_body['movie_id'])
		rating = int(the_body['rating'])

		try:
			mdb.set_user_movie_rating(uid, mid, rating)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)



class RatingsController(object):

	def GET(self, key):
		output = {'result':'success'}
		mid = int(key)
		output['movie_id'] = mid

		try:
			output['rating'] = mdb.get_rating(mid)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

class ResetController(object):

	def RESET_ALL(self):
		output = {'result':'success'}
		mdb.load_movies('ml-1m/movies.dat')
		mdb.load_users('ml-1m/users.dat')
		mdb.load_ratings('ml-1m/ratings.dat')
		mdb.load_images()

		return json.dumps(output)

	def RESET(self, key):
		output = {'result':'success'}
		mdb.load_movie('ml-1m/movies.dat', int(key))

