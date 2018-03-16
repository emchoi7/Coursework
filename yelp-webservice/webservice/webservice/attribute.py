import cherrypy
import json, re
import _yelp_database

class AttributeController(object):
	def __init__(self, ydb):
		self.ydb = ydb

	def GET(self, attribute):
		output = {"result" : "success"}
		attribute = str(attribute)
		try:
			output = self.ydb.view_top_review(attribute)
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)

	def GET_LOC(self, attribute, location):
		output = {"result" : "success"}
		attribute = str(attribute)
		location = str(location)
		try:
			output = self.ydb.view_location_top_review(location, attribute)
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)

	def GET_BIZ(self, attribute, bid):
		output = {"result" : "success"}
		attribute = str(attribute)
		bid = str(bid)
		try:
			output = self.ydb.view_biz_top_review(bid, attribute)
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)		
