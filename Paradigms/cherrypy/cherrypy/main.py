#Eugene Choi
import cherrypy
from controller import *

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	moviesController = MoviesController()
	midController = MIDController()
	userController = UserController()
	uidController = UIDController()
	recController = RecController()
	ratingsController = RatingsController()
	resetController = ResetController()

	dispatcher.connect('movies_get','/movies/',
		controller=moviesController,
		action = 'GET',
		conditions=dict(method=['GET']))

	dispatcher.connect('movies_post','/movies/',
		controller=moviesController,
		action = 'POST',
		conditions=dict(method=['POST']))

	dispatcher.connect('movies_delete', '/movies/', 
		controller=moviesController,
		action = 'DELETE',
		conditions=dict(method=['DELETE']))

	dispatcher.connect('mid_get', '/movies/:key', 
		controller=midController,
		action = 'GET',
		conditions=dict(method=['GET']))

	dispatcher.connect('mid_put','/movies/:key',
		controller=midController,
		action = 'PUT',
		conditions=dict(method=['PUT']))

	dispatcher.connect('mid_delete', '/movies/:key', 
		controller=midController,
		action = 'DELETE',
		conditions=dict(method=['DELETE']))

	dispatcher.connect('users_get','/users/',
		controller=userController,
		action = 'GET',
		conditions=dict(method=['GET']))

	dispatcher.connect('users_post','/users/',
		controller=userController,
		action = 'POST',
		conditions=dict(method=['POST']))

	dispatcher.connect('users_delete','/users/',
		controller=userController,
		action = 'DELETE',
		conditions=dict(method=['DELETE']))

	dispatcher.connect('uid_get','/users/:key',
		controller=uidController,
		action = 'GET',
		conditions=dict(method=['GET']))

	dispatcher.connect('uid_put','/users/:key',
		controller=uidController,
		action = 'PUT',
		conditions=dict(method=['PUT']))

	dispatcher.connect('uid_delete','/users/:key',
		controller=uidController,
		action = 'DELETE',
		conditions=dict(method=['DELETE']))

	dispatcher.connect('rec_get','/recommendations/:key',
		controller=recController,
		action = 'GET',
		conditions=dict(method=['GET']))

	dispatcher.connect('rec_put','/recommendations/:key',
		controller=recController,
		action = 'PUT',
		conditions=dict(method=['PUT']))

	dispatcher.connect('rec_delete','/recommendations/',
		controller=recController,
		action = 'DELETE',
		conditions=dict(method=['DELETE']))

	dispatcher.connect('ratings_get','/ratings/:key',
		controller=ratingsController,
		action = 'GET',
		conditions=dict(method=['GET']))

	dispatcher.connect('reset_all','/reset/',
		controller=resetController,
		action = 'RESET_ALL',
		conditions=dict(method=['PUT']))

	dispatcher.connect('reset','/reset/:key',
		controller=resetController,
		action = 'RESET',
		conditions=dict(method=['PUT']))


	conf = {'global' : {'server.socket_host':'student04.cse.nd.edu',
							'server.socket_port':51022},
						'/' : {'request.dispatch':dispatcher} }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)




if __name__ == '__main__':
	start_service()