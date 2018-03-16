import json

class _yelp_database:
	def __init__(self):
		self.bizs = {} #for businesses { business_id#:{ business_id:######, name:"name", ...}}
		self.reviews = {} #for reviews

	def load_bizs(self, bizfile): #takes in the yelp business.json file
		with open(bizfile) as handle:
			for line in handle:
				data = json.loads(line)
				self.bizs[data["business_id"]] = data

	def get_biz(self,bid):
		bid = str(bid)
		try:
			return self.bizs[bid]
		except KeyError as ex:
			return None

	def get_location(self, bid):
		bid = str(bid)
		try:
			return self.bizs[bid]['postal_code']
		except KeyError as ex:
			return None

	def load_reviews(self, revfile):
		with open(revfile) as handle:
			for line in handle:
				data = json.loads(line)
				self.reviews[data["review_id"]] = data

	def get_review(self, rid):
		rid = str(rid)
		try:
			return self.reviews[rid]
		except KeyError as ex:
			return None

	def get_biz_reviews(self, bid):
		bid = str(bid)
		biz_reviews = {}
		try:
			for rid in self.reviews.keys():
				if self.reviews[rid]["business_id"] == bid:
					biz_reviews[rid] = self.reviews[rid]
			return biz_reviews
		except KeyError as ex:
			return None

	def get_location_biz(self, location): #gets businesses given the location (postal_code)
		loc_biz = {}
		for bid in self.bizs.keys():
			if self.bizs[bid]['postal_code'] == location:
				loc_biz[bid] = self.bizs[bid]
		return loc_biz

	def view_top_review(self, attribute): #get the review with highest [cool, funny, useful] rating
		max_rating = 0
		top_review = {}
		for rid in self.reviews.keys():
			if self.reviews[rid][attribute] > max_rating:
				max_rating = self.reviews[rid][attribute]
				top_review = self.reviews[rid]
		return top_review

	def view_location_top_review(self, location, attribute): #gets top review given location
		max_rating = 0
		top_review = {}
		biz = self.get_location_biz(location)
		for rid in self.reviews.keys(): #for each review,
			for bid in biz.keys(): #for each business in the given location,
				if self.reviews[rid]['business_id'] == bid: #if the review is for a business within the location,
					if self.reviews[rid][attribute] > max_rating: #if the vote for the attribute is greater than the current max_rating,
						max_rating = self.reviews[rid][attribute] #set max_rating to the number of votes current review has for the attribute
						top_review = self.reviews[rid] #set the top_review to the current review
		return top_review

	def view_biz_top_review(self, bid, attribute): #gets top review given business
		max_rating = 0
		top_review = {}
		for rid in self.reviews.keys():
			if self.reviews[rid]['business_id'] == bid:
				if self.reviews[rid][attribute] > max_rating:
					max_rating = self.reviews[rid][attribute]
					top_review = self.reviews[rid]
		return top_review

	def rate_review(self, rid, attribute):
		self.reviews[rid][attribute] += 1

if __name__ == "__main__":
	ydb = _yelp_database()
	ydb.load_bizs('dataset/business.json')
	ydb.load_reviews('dataset/review.json')
	postal = ydb.get_location_biz('89108')
	print(postal)
