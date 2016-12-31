from contextlib import suppress
import json
import sys
import dbm
class DataBase(object):
    '''A wrapper around the built in dbm library. This class uses json
to allow for non-string data to be stored in the database'''
    def __init__(self, dbname, maxcache=10**8):
        '''Create a database using given database name and use a cache with a
specified maximium size
'''
        self.dbname=dbname
        self.db=dbm.open(dbname, 'c')
        self.maxcache=maxcache
        self.cache={}
    def __setitem__(self, key, value):
        self.checksize()
        self.cache[key]=value
        self.commit()
    def __getitem__(self, key):
        self.checksize()
        with suppress(KeyError):
            return self.cache[key]
        with suppress(KeyError):
            res=self.db[json.dumps(key)].decode('utf-8')
            res=json.loads(res)
            self.cache[key]=res
            return res
        raise KeyError(key)
    def __delitem__(self, key):
        with suppress(KeyError):
            del self.db[json.dumps(key)]
        with suppress(KeyError):
            del self.cache[key]
    def __contains__(self, key):
        self.checksize()
        if key in self.cache:
            return True
        if key in self.db:
            self.cache[key]=json.loads(self.db[json.dumps(key)].decode('utf-8'))
            return True
        return False
    def __iter__(self):
        for i in self.cache:
            yield i
        for i in self.db.keys():
            i=json.loads(i.decode('utf-8'))
            if i not in self.cache:
                yield i
    def keys(self):
        return iter(self)
    def update(self, E, **F):
        self.checksize()
        self.cache.update(E, **F)
    def checksize(self):
        if sys.getsizeof(self.cache)>self.maxcache:
            print('Cache size exeeded')
            self.commit()
    def commit(self):
        '''Save all changes to file and clear the cache'''
        for key in self.cache:
            self.db[json.dumps(key)]=json.dumps(self.cache[key])
        self.db.close()
        del self.cache
        self.__init__(self.dbname, self.maxcache)
