import cherrypy
import json, re
import _yelp_database

class BusinessController(object):
	def __init__(self, ydb):
		self.ydb = ydb

	def GET(self):
		output = {"result" : "success"}
		try:
			output = {}
			output.update(self.ydb.bizs)
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)


	def GET_BID(self, bid):
		output = {"result" : "success"}
		bid = str(bid)
		try:
			output.update(self.ydb.get_biz(bid))
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)