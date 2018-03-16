import requests
import json

class _webservice_primer:
	def __init__(self):
		self.SITE_URL = 'http://student04.cse.nd.edu:51001'
		self.MOVIES_URL = self.SITE_URL + '/movies/'
		self.RESET_URL = self.SITE_URL + '/reset/'

	def get_movie(self, mid):
		r = requests.get(self.MOVIES_URL + str(mid))
		resp = json.loads(r.content)
		return resp

	def set_movie_title(self, mid, title):
		movie = self.get_movie(mid)
		movie['title'] = title
		r = requests.put(self.MOVIES_URL + str(mid),data=json.dumps(movie))

	def delete_movie(self, mid):
		r = requests.delete(self.MOVIES_URL + str(mid), data=json.dumps({'mid':mid}))


	def reset_movie(self, mid):
		r = requests.put(self.RESET_URL + str(mid),data=json.dumps({}))



if __name__ == "__main__":
	MID = 22
	ws = _webservice_primer()
	ws.set_movie_title(MID, 's')
	movie = ws.get_movie(MID)
	if movie['result'] == 'success':
		print("Title:\t%s" % movie['title'])

	else:
		print("Error:\t%s" % movie['message'])
