
This project took the provided yelp datasets businesses and reviews and turned it into a database which is then used by a webservice(written to be run on a ND student port- unfortunately, do not have access to it anymore). The web client is built with mostly JavaScript to take in a zip code (or none) and an attribute which filters the reviews. The page then displays a review and provides the user with buttons (cool, funny, useful) that they can rate the review with. A side bar is shown as well that shows the metadata for the review. If the user desires, they can look for more reviews based on the business of the current review. 

The backend was entirely written in python. The database uses yelp’s given json files to parse data into a dictionary of its own. The webservice uses cherrypy. 

———————————original project readme document———————————
Eugene Choi
Maria Beatriz Zanardo

Final Project

_yelp_database.py first organizes data into two dictionaries: bizs and reviews. Because the data files were too large, we had to make scripts for each data file to parse through the information we wanted. We first created the file with business information. Then, we went through all the reviews that were made for those businesses we had in our business file.
The database code has basic functions such as load_bizs, get_biz, get_location (gets postal code of certain business), load_reviews, get_review, get_biz_reviews(returns al the reviews for a business), get_location_biz(returns businesses in given location), view_top_review(gets the review with highest votes for given attribute), view_location_top_review(gets the review with highest votes for given attribute and location), view_biz_top_review(gets the review with highest votes for given attribute and business).
It also has rate_review which adds 1 to a review's rating of given attribute (funny, cool, useful). Delete_review deletes a review from the reviews dictionary.

In our webservice, here are all the requests that can be made:
RESET:
'PUT': /reset/, resets the database

BUSINESS:
'GET': /business/, returns the whole bizs dict
'GET': /business/:bid, returns the information on given business

REVIEWS:
'GET': /reviews/:rid, returns information on given review
'GET': /reviews/, returns the whole reviews dict
'PUT': /reviews/:rid, rates given review
'DELETE': /reviews/:rid, deletes given review from database

BUSINESS_REVIEWS:
'GET': /business_reviews/:bid/attribute/:attribute, returns the top review for given business for given attribute

LOCATIONS:
'GET': /location/:location, returns businesses in a given location

ATTRIBUTE:
'GET': /attribute/:attribute, gets the top review for given attribute
'GET': /attribute/:attribute/location/:location, gets the top review for given location and attribute
'GET': /attribute/:attribute/business/:bid, gets the top review for given attribute and business


Our webclient (http://student04.cse.nd.edu/echoi7/yelp_review_rater/) retrieves information from the database through the webservice we created. The user can input the attribute and optionally a zipcode/postal_code. When the user submits, the review appears, and they can see what they are seeing the reviews based on. The information about the business being reviewed is shown to the right of the review. The user can then rate the review 'funny', 'cool', or 'useful'. Or, the user can also choose to view reviews of the business or reviews of businesses in the location of the business, given an attribute. 

