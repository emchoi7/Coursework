import cherrypy
import json, re
import _yelp_database

class OptionsController(object):

	def OPTIONS(self, *args, **kargs):
		return ""