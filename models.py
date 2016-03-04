from google.appengine.ext import ndb

class Counter(ndb.Model):
    name = ndb.StringProperty()
    count = ndb.IntegerProperty()
