#Eugene Choi

class _movie_database:

    def __init__(self):
      # your code here
      self.movies   = {}
      self.users  = {}
      self.ratings  = {}
      self.images = {}
      self.avgrating = [] # list with items: {mid: list of users that rated, avgrating}

    def load_images(self):
      imagefiles = open('/home/paradigms/images.dat')
      for file in imagefiles:
        a = file.split("::")
        self.images[int(a[0])] = a[2].rstrip()


    def load_movies(self, movie_file):
      movietitles = open(movie_file)
      for title in movietitles:  
        a = title.split("::")
        data = []
        data.append(a[1])
        data.append(a[2].rstrip('\n'))
        self.movies[int(a[0])] = data

    def load_movie(self, movie_file, mid):
      movietitles = open(movie_file)
      for title in movietitles:  
        a = title.split("::")
        if mid == int(a[0]):
          data = []
          data.append(a[1])
          data.append(a[2].rstrip('\n'))
          self.movies[mid] = data

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

    def get_highest_unrated_movie(self, uid):
        unrated = {} #{mid : rating}
        for mid in self.ratings:
          if uid not in self.ratings[mid]:
            unrated[mid] = self.get_rating(mid)
        highest = max(unrated.values())
        highestid = 0

        for mid in unrated:
          if unrated[mid] == highest:
            if highestid == 0:
              highestid = mid
            else:
              if highestid > mid:
                highestid = mid

        return highestid


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
       mdb.load_images()
       print(mdb.get_highest_unrated_movie(149))
       #print(mdb.avgrating[0])
       #print(mdb.get_user_movie_rating(1573, 22))
       #print(mdb.get_user_movie_rating(1572, 22))
       #mdb.delete_all_ratings()

