import unittest
import requests
import json

class Tests (unittest.TestCase):

	PORT_NUM = '51022'
	print("Testing Port number: ", PORT_NUM)
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	RESET_URL = SITE_URL + '/reset/'
	BUSINESS_URL = SITE_URL + '/business/'
	REVIEWS_URL = SITE_URL + '/reviews/'
	BIZREV_URL = SITE_URL + '/business_reviews/'
	LOCATION_URL = SITE_URL + '/location/'
	ATTRIBUTE_URL = SITE_URL + '/attribute/'
	LOCATION =  '/location/'
	BUSINESS = '/business/'

	def reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL, data = json.dumps(m))

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False


	# business tests

	def test_bid_get(self):
	 	self.reset_data()
	 	bid = 'PjQngP_7m7PA8K1WUHdXqg'
	 	r = requests.get(self.BUSINESS_URL + str(bid))
	 	self.assertTrue(self.is_json(r.content.decode('utf-8')))
	 	resp = json.loads(r.content.decode('utf-8'))
	 	self.assertEqual(resp['name'], 'RETRO Dog')

	def test_business_get(self):
	 	self.reset_data()
	 	r = requests.get(self.BUSINESS_URL)
	 	self.assertTrue(self.is_json(r.content.decode('utf-8')))
	 	resp = json.loads(r.content.decode('utf-8'))
	 	bid = 'PjQngP_7m7PA8K1WUHdXqg'
	 	biz = resp[bid]
	 	self.assertEqual(biz['name'], 'RETRO Dog')

#
#	# # reviews tests
#
	def test_rid_get(self):
	 	self.reset_data()
	 	rid = 'VfBHSwC5Vz_pbFluy07i9Q'
	 	r = requests.get(self.REVIEWS_URL + str(rid))
	 	self.assertTrue(self.is_json(r.content.decode('utf-8')))
	 	resp = json.loads(r.content.decode('utf-8'))
	 	#print(resp)
	 	self.assertEqual(resp['business_id'], 'uYHaNptLzDLoV_JZ_MuzUA')

	def test_reviews_get(self):
	 	self.reset_data()
	 	r = requests.get(self.REVIEWS_URL)
	 	self.assertTrue(self.is_json(r.content.decode()))
	 	resp = json.loads(r.content.decode())
	 	rid = 'VfBHSwC5Vz_pbFluy07i9Q'
	 	review = resp[rid]
	 	self.assertEqual(review['user_id'], 'cjpdDjZyprfyDG3RlkVG3w')

	def test_reviews_put(self):
	 	self.reset_data()
	 	rid = "VfBHSwC5Vz_pbFluy07i9Q"
	 	m = {"review_id" : rid, "attribute" : "useful"}
	 	rput = requests.put(self.REVIEWS_URL + str(rid), data = json.dumps(m))
	 	self.assertTrue(self.is_json(rput.content.decode('utf-8')))
	 	resp_put = json.loads(rput.content.decode('utf-8'))
	 	self.assertEqual(resp_put['result'], 'success')

	 	rget = requests.get(self.REVIEWS_URL + str(rid))
	 	resp_get = json.loads(rget.content.decode('utf-8'))
	 	self.assertEqual(resp_get['useful'], 1)

	def test_rid_del(self):
		self.reset_data()
		rid = "VfBHSwC5Vz_pbFluy07i9Q"
		rdel = requests.delete(self.REVIEWS_URL + str(rid))
		resp = json.loads(rdel.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.REVIEWS_URL + str(rid))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'error')

	# business_review tests

	def test_biz_rev_get(self):
		self.reset_data()
		bid = 'PjQngP_7m7PA8K1WUHdXqg'
		r = requests.get(self.BIZREV_URL + str(bid) + '/attribute/' + 'funny')
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['user_id'], 'VOUnXOlll52vwQcJK1tm8A')

	# location tests

	def test_loc_get(self):
		self.reset_data()
		location = '28213'
		r = requests.get(self.LOCATION_URL + str(location))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		#print(resp)
		self.assertEqual(resp['ShnXvNkJKsDIQaGJeM0L6w']['business_id'], 'ShnXvNkJKsDIQaGJeM0L6w' )

	# attribute tests
	def test_attr_get(self):
		self.reset_data()
		attribute = 'funny'
		r = requests.get(self.ATTRIBUTE_URL + str(attribute))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['review_id'], 'Oxz26pqpIb7dDVeuUzNZlg')

	def test_attr_loc_get(self):
		self.reset_data()
		location = '28213'
		attribute = 'funny'
		r = requests.get(self.ATTRIBUTE_URL + str(attribute) + self.LOCATION + str(location))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['review_id'], 'WWF2O94KLFL18o_fYceOHg')

	def test_attr_biz_get(self):
		self.reset_data()
		location = '28213'
		attribute = 'funny'
		bid = 'ShnXvNkJKsDIQaGJeM0L6w'
		r = requests.get(self.ATTRIBUTE_URL + str(attribute) + self.BUSINESS + str(bid))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['review_id'], 'WWF2O94KLFL18o_fYceOHg')


if __name__ == "__main__":
	unittest.main()





