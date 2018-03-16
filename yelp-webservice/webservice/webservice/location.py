import cherrypy
import json, re
import _yelp_database

class LocationController(object):
	def __init__(self, ydb):
		self.ydb = ydb

	def GET_LOC(self, location):
		output = {"result" : "success"}
		location = str(location)
		try:
			bizs = self.ydb.get_location_biz(location)
			output.update(bizs)
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)