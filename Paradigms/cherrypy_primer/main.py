#Eugene Choi
import cherrypy
from dcont import *

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	dictionaryController = DictionaryController()

	dispatcher.connect('dict_get','/dictionary/',
		controller=dictionaryController,
		action = 'GET',
		conditions=dict(method=['GET']))

	dispatcher.connect('dict_post','/dictionary/',
		controller=dictionaryController,
		action = 'POST',
		conditions=dict(method=['POST']))

	dispatcher.connect('dict_put','/dictionary/:key',
		controller=dictionaryController,
		action = 'PUT',
		conditions=dict(method=['PUT']))

	dispatcher.connect('dict_kget', '/dictionary/:key', 
		controller=dictionaryController,
		action = 'KGET',
		conditions=dict(method=['GET']))

	dispatcher.connect('dict_delete', '/dictionary/:key', 
		controller=dictionaryController,
		action = 'DELETE',
		conditions=dict(method=['DELETE']))

	dispatcher.connect('dict_deleteall', '/dictionary/', 
		controller=dictionaryController,
		action = 'DELETEALL',
		conditions=dict(method=['DELETE']))

	conf = {'global' : {'server.socket_host':'student04.cse.nd.edu',
							'server.socket_port':51022},
						'/' : {'request.dispatch':dispatcher} }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)




if __name__ == '__main__':
	start_service()