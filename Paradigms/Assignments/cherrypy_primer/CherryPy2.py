import cherrypy
import json

#####NEW CODE#####
class DictionaryKeyController(object):

	def GET(self, key):
		#rule 1: definitely want to have default output
		output = {"result":"success"}

		#rule2: check your input data before you use it!!
		key = int(key) #make sure right datatype (maybe int, maybe str)
		the_body = cherrypy.request.body.read().decode()

		#rule 3: try-except anything that can cause an exception/anything that can fail
		try:
			the_body = json.loads(the_body)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output) 
#####NEW CODE######

class MyController(object): #object is one class that all other classes inherit from; 
							#the common python object
							#means that MyController is nothing special
	def GET(self, thetype): #handler when using get request
	#First rule: some kind of output that you send; 
	#send at least result:success or result:failure if needs response
		output = {"result":"success"} 
		my_dictionary = {thetype:"quack"}
		return json.dumps(my_dictionary)


def start_service():
	mycontroller = MyController() #new comment# have diff controller for keycontroller, 
								#connect them by using same dispatcher

	#what will allow request to connect to handler
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	
	dispatcher.connect('duckconnection',
		'/animals/:thetype',
		controller=mycontroller,
		action='GET', #GET from MyController; the handler from class we access
		conditions=dict(method=['GET'])) #This is http type of get) 
	#Config for server
	conf = {
		'global':{
			'server.socket_host':'student04.cse.nd.edu'
			'server.socket_port': 51010
		}, #THIS COMMA DOE
		'/':{ 'request.dispatch' : dispatcher}
	}
	#Start server
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app) #starts webservice

	if __name__ == '__main__':
		start_service()



#404 is response that comes back from the server
#means that the server is up and running but doesn't know what to do
#since we didn't tell it what to do
#ps (check if process running); kill if still running bc it will occupy port 