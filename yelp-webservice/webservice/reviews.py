import cherrypy
import json, re
import _yelp_database

class ReviewsController(object):
	def __init__(self, ydb):
		self.ydb = ydb

	def GET(self):
		output = {"result" : "success"}
		try:
			output.update(self.ydb.reviews)
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)

	def GET_RID(self, rid):
		output = {"result" : "success"}
		rid = str(rid)
		try:
			output = self.ydb.get_review(rid)
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)

	def PUT(self, rid):
		output = {"result" : "success"}
		rid = str(rid)
		try:
			body = cherrypy.request.body.read().decode()
			data = json.loads(body)
			attribute = data["attribute"]
			self.ydb.rate_review(rid, attribute)
			output = {"result" : "success"}
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)

