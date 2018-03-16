import json
import cherrypy


class DictionaryController(object):
	def __init__(self):
		self.myd = dict()

	def GET(self):
		#default output
		output = {'result':'success'}
		entries = []
		for key in self.myd:
			entries.append({'key':key, 'value':self.myd[key]})
		#try-except
		try:
			output['entries'] = entries
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'

		return json.dumps(output)

	def PUT(self, key):
		output = {'result':'success'}
		key = str(key)
		the_body = json.loads(cherrypy.request.body.read())

		try:
			self.myd[key] = the_body['value']
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)


	def POST(self):
		output = {'result':'success'}
		the_body = json.loads(cherrypy.request.body.read())
		key = the_body['key']

		try:
			self.myd[key] = the_body['value']
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)


	def KGET(self, key):
		#rule 1: definitely want to have default output
		output = {"result":"success"}

		#rule2: check your input data before you use it!!
		key = str(key)

		print(self.myd)

		#rule 3: try-except anything that can cause an exception/anything that can fail
		try:
			output['key'] = key
			output['value'] = self.myd[key]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)


	def DELETE(self, key):
		output = {"result":"success"}

		try:
			del self.myd[key]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETEALL(self):
		output = {"result":"success"}

		self.myd = dict()

		return json.dumps(output)






