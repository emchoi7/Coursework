import cherrypy
import json, re
from _yelp_database import _yelp_database
from reset import ResetController
from business import BusinessController
from reviews import ReviewsController
from location import LocationController
from bizreviews import BizReviewsController
from attribute import AttributeController
from options import OptionsController

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Headers"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

def start_service():
	ydb = _yelp_database()
	ydb.load_bizs('dataset/business.json')
	ydb.load_reviews('dataset/review.json')
	resetController = ResetController(ydb)
	businessController = BusinessController(ydb)
	reviewsController = ReviewsController(ydb)
	locationController = LocationController(ydb)
	bizreviewController = BizReviewsController(ydb)
	attributeController = AttributeController(ydb)
	optController = OptionsController()
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	# reset
	dispatcher.connect('reset', '/reset/', controller=resetController,
                        action = 'PUT', conditions=dict(method=['PUT']))

	# business
	dispatcher.connect('bid_get', '/business/:bid', controller=businessController,
                        action = 'GET_BID', conditions=dict(method=['GET']))

	dispatcher.connect('business_get', '/business/', controller=businessController,
                        action = 'GET', conditions=dict(method=['GET']))

	# reviews
	dispatcher.connect('rid_get', '/reviews/:rid', controller=reviewsController,
                        action = 'GET_RID', conditions=dict(method=['GET']))


	dispatcher.connect('reviews_get', '/reviews/', controller=reviewsController,
                        action = 'GET', conditions=dict(method=['GET']))

	dispatcher.connect('rid_put', '/reviews/:rid', controller=reviewsController,
                        action = 'PUT', conditions=dict(method=['PUT']))	

	dispatcher.connect('rid_del', '/reviews/:rid', controller=reviewsController,
                        action = 'DEL_REV', conditions=dict(method=['DELETE']))

	# business_reviews
	dispatcher.connect('biz_rev_get', '/business_reviews/:bid', controller=bizreviewController,
                        action = 'GET_BID', conditions=dict(method=['GET']))
	
	# locations
	dispatcher.connect('loc_get', '/location/:location', controller=locationController,
                         action = 'GET_LOC', conditions=dict(method=['GET']))

	# attribute
	dispatcher.connect('attr_get', '/attribute/:attribute', controller=attributeController,
                        action = 'GET', conditions=dict(method=['GET']))

	dispatcher.connect('attr_loc_get', '/attribute/:attribute/location/:location', controller=attributeController,
                        action = 'GET_LOC', conditions=dict(method=['GET']))

	dispatcher.connect('attr_biz_get', '/attribute/:attribute/business/:bid', controller=attributeController,
                        action = 'GET_BIZ', conditions=dict(method=['GET']))

	###CORS###
	dispatcher.connect('opt_reset','/reset/',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_bid_get','/business/:bid',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_business_get','/business/',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_rid_get','/reviews/:rid',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_reviews_get','/reviews/',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_rid_put','/reviews/:rid',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_rid_del','/reviews/:rid',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_biz_rev_get','/business_reviews/:bid',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_loc_get','/location/:location',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_attr_get','/attribute/:attribute',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_attr_loc_get','/attribute/:attribute',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))
	dispatcher.connect('opt_biz_get','/attribute/:attribute',
		controller=optController,
		action = 'OPTIONS',
		conditions=dict(method=['OPTIONS']))

	conf = {'global' : {'server.socket_host':'student04.cse.nd.edu',
							'server.socket_port':51022},
						'/' : {
								'request.dispatch':dispatcher,
								'tools.CORS.on': True
								} 
						}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)


if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()


