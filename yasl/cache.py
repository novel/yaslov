import os
import os.path
import sqlite3 as db

from xdg import BaseDirectory

class Cache(object):

    def __init__(self):
        cache_file = self._init_paths()
        self._conn, self._cur = self._init_db(cache_file)

    def _init_paths(self):
        """Checks if the cache exists, create it if
        it doesn't"""
        self._cache_dir = os.path.join(BaseDirectory.xdg_cache_home,
                "yaslov")
        
        if not os.path.isdir(self._cache_dir):
            os.makedirs(self._cache_dir, 0700)
        
        return os.path.join(self._cache_dir, "cache.db")

    def _init_db(self, cache_file):
        """Initializes the database."""
        conn = db.connect(cache_file)
        cur = conn.cursor()

        cur.execute("PRAGMA foreign_keys = 1;")

        cur.executescript("""
            CREATE TABLE IF NOT EXISTS requests(
                id INTEGER PRIMARY KEY ASC,
                request TEXT NOT NULL,
                response TEXT);

            CREATE INDEX IF NOT EXISTS i2 ON requests(request);

            CREATE TABLE IF NOT EXISTS timestamp(
                request_id REFERENCES requests(id),
                timestamp INTEGER NOT NULL);
            """)
        conn.commit()

        return conn, cur

    def find(self, request):
        self._cur.execute("SELECT response FROM requests WHERE request=?",
                (request,))
        try:
            return self._cur.fetchone()[0]
        except TypeError:
            return None

    def add(self, request, response):
        self._cur.execute("""INSERT INTO requests(request, response)
            VALUES (?, ?)""", (request, response))
        self._conn.commit()

    def update(self, request):
        self._cur.execute("SELECT id FROM requests WHERE request=?",
                (request,))
        _id = self._cur.fetchone()[0]
        
        self._cur.execute("""INSERT INTO timestamp(request_id, timestamp)
            VALUES(?, strftime('%s','now'))""", (_id,))
        self._conn.commit()
