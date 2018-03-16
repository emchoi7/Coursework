import cherrypy
import json, re
import _yelp_database

class BizReviewsController(object):
	def __init__(self, ydb):
		self.ydb = ydb

	def GET_BID(self, bid, attribute):
		output = {"result" : "success"}
		bid = str(bid)
		try:
			bizs = self.ydb.view_biz_top_review(bid, attribute)
			output.update(bizs)
			output["result"] = "success"
		except Exception as ex:
			output = {"result" : "error"}
			output["message"] = str(ex)
		return json.dumps(output)
