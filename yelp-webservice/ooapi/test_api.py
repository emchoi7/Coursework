from _yelp_database import _yelp_database
import unittest

class TestYelpDatabase(unittest.TestCase):
	ydb = _yelp_database()

	def reset_data(self):
		self.ydb.load_bizs('dataset/business.json')
		self.ydb.load_reviews('dataset/review.json')

	def test_get_biz(self):
		self.reset_data()
		biz = self.ydb.get_biz('PjQngP_7m7PA8K1WUHdXqg')
		self.assertEqual(biz['name'], 'RETRO Dog')

	def test_get_location(self):
		#self.reset_data()
		biz = self.ydb.get_location('PjQngP_7m7PA8K1WUHdXqg')
		self.assertEqual(biz, '44224')

	def test_get_review(self):
		#self.reset_data()
		review = self.ydb.get_review('VfBHSwC5Vz_pbFluy07i9Q')
		self.assertEqual(review['user_id'], 'cjpdDjZyprfyDG3RlkVG3w')

	def test_get_biz_reviews(self):
		#self.reset_data()
		reviews = self.ydb.get_biz_reviews('uYHaNptLzDLoV_JZ_MuzUA')
		self.assertEqual(reviews['VfBHSwC5Vz_pbFluy07i9Q']['user_id'], 'cjpdDjZyprfyDG3RlkVG3w')

	def test_get_location_biz(self):
		#self.reset_data()
		biz = self.ydb.get_location_biz('44224')
		self.assertEqual(biz['PjQngP_7m7PA8K1WUHdXqg']['name'], 'RETRO Dog' )



if __name__ == "__main__":
    unittest.main()