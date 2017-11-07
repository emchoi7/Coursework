#Eugene Choi
#Assumed I didn't have to put movies.dat into the dropbox

class _movie_database:

    def __init__(self):
      # your code here
      self.movies   = {}
      self.users  = {}
      self.ratings  = {}

    def load_movies(self, movie_file):
      movietitles = open(movie_file)
      for title in movietitles:  
        a = title.split("::")
        data = []
        data.append(a[1])
        data.append(a[2].rstrip('\n'))
        self.movies[int(a[0])] = data

    def get_movie(self, mid):
      i = 0
      for key in self.movies.keys():
        if mid == key:
          return self.movies[mid]

        i = i + 1

        if i == len(self.movies):
          return None

    def get_movies(self):
      return self.movies.keys()

    def set_movie(self, mid, data):
      self.movies[mid] = data

    def delete_movie(self, mid):
      i = 0
      for key in list(self.movies.keys()):
        if mid == key:
          del self.movies[mid]

    def load_users(self, users_file):
      users = open(users_file)
      for user in users:  
        a = user.split("::")
        data = []
        data.append(a[1]) #gender
        data.append(int(a[2])) #age
        data.append(int(a[3])) #occupation
        data.append(a[4].rstrip('\n')) #zipcode
        self.users[int(a[0])] = data

    def get_user(self, uid):
      i = 0
      for key in self.users.keys():
        if uid == key:
          return self.users[uid]

        i = i + 1

        if i == len(self.users):
          return None

    def get_users(self):
      return self.users.keys()

    def set_user(self, uid, data):
      self.users[uid] = data

    def delete_user(self, uid):
      i = 0
      for key in list(self.users.keys()):
        if uid == key:
          del self.users[uid]

    def load_ratings(self, ratings_file):
      ratings = open(ratings_file)
      for rating in ratings:  
        a = rating.split("::")
        if int(a[1]) in self.ratings.keys():
          self.ratings[int(a[1])][int(a[0])] = int(a[2])
        else:
          self.ratings[int(a[1])] = {}
          self.ratings[int(a[1])][int(a[0])] = int(a[2])


    def get_rating(self, mid):
      totnum = 0
      sumnum = 0
      avg = 0
      try: 
        for v in self.ratings[mid].values():
          totnum += 1
          sumnum += v
        avg = sumnum/totnum
      except Exception:
        pass

      return avg

    def get_highest_rated_movie(self):
      ratings = {} #holds {rating : mid}
      for mid in self.movies.keys(): #look through all mids
        rating = self.get_rating(mid)
        ratings[mid] = rating
      highest = max(ratings, key=ratings.get)
      return highest

    def set_user_movie_rating(self, uid, mid, rating):
      for k in self.ratings.keys(): #look through all mid
        for m in self.ratings[k].keys(): #look through all uid for each mid
          if uid == m or mid == k:
            self.ratings[mid][uid] = rating
              

    def get_user_movie_rating(self, uid, mid):
      mkeys = list(self.ratings.keys())

      if mid in mkeys:
        ukeys = list(self.ratings[mid].keys())
        if uid in ukeys:
          return self.ratings[mid][uid]
        else:
          return None
      else:
        return None

    def delete_all_ratings(self):
      self.ratings = {}

#def print_sorted_movies(self):
#  sorted_movies = sorted(self.movies)
#  for movie in sorted_movies:
#    print(movie)

if __name__ == "__main__":
       mdb = _movie_database()

       #### MOVIES ########
       mdb.load_movies('ml-1m/movies.dat')
       mdb.load_users('ml-1m/users.dat')
       mdb.load_ratings('ml-1m/ratings.dat')
       mid = mdb.get_highest_rated_movie()
       print(mdb.get_rating(mid))
       #print(mdb.get_user_movie_rating(1573, 22))
       #print(mdb.get_user_movie_rating(1572, 22))
       #mdb.delete_all_ratings()

