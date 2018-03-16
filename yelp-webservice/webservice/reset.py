import cherrypy
import json, re
import _yelp_database

class ResetController(object):
    def __init__(self, ydb):
        self.ydb = ydb

    def PUT(self):
        output = {"result" : "success"}
        try:
            self.ydb.load_bizs('dataset/business.json')
            self.ydb.load_reviews('dataset/review.json')
        except Exception as ex:
            output["result"] = "error"
            output["message"] = str(ex)

        return json.dumps(output)