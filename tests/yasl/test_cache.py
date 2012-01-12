from nose.tools import *
from mock import patch, Mock

from yasl.cache import Cache


class TestCache(object):

    @patch('os.makedirs')
    @patch('os.path')
    @patch.object(Cache, '__init__')
    def test__init_paths_creates_dir_if_needed(self,
            mock_cache_init, mock_os_path, mock_os_makedirs):
        mock_cache_init.return_value = None

        fake_dirname = "testdir"

        mock_os_path.join.return_value = fake_dirname
        mock_os_path.isdir.return_value = False

        cache = Cache()
        
        cache_path = cache._init_paths()

        assert_equal(cache_path, fake_dirname)

        mock_os_path.isdir.assert_called_with(fake_dirname)
        mock_os_makedirs.assert_called_with(fake_dirname, 0700)

    @patch('os.makedirs')
    @patch('os.path')
    @patch.object(Cache, '__init__')
    def test__init_paths_not_creates_dir_if_it_exists(self,
            mock_cache_init, mock_os_path, mock_os_makedirs):
        mock_cache_init.return_value = None

        fake_dirname = "testdir"

        mock_os_path.join.return_value = fake_dirname
        mock_os_path.isdir.return_value = True

        cache = Cache()
        
        cache_path = cache._init_paths()

        assert_equal(cache_path, fake_dirname)

        mock_os_path.isdir.assert_called_with(fake_dirname)
        assert_false(mock_os_makedirs.called)

    @patch.object(Cache, '_init_paths')
    def test__init_db_creates_all_the_tables(self, mock_cache_init_paths):
        expected_tables = set([u'requests', u'timestamp'])
        mock_cache_init_paths.return_value = ":memory:"

        cache = Cache()

        cache._cur.execute("""SELECT name FROM sqlite_master
                WHERE type='table'""")
        actual_tables = set([i[0] for i in cache._cur.fetchall()])
        assert_equal(actual_tables, expected_tables)

    @patch.object(Cache, '_init_paths')
    def test_add_and_find(self, mock_cache_init_paths):
        mock_cache_init_paths.return_value = ":memory:"

        cache = Cache()
        
        request = "request"
        response = "sample response"
        cache.add(request, response)

        cache._cur.execute("""SELECT * FROM requests
            WHERE request=? AND response=?""", (request, response))
        assert_equals(len(cache._cur.fetchall()), 1)

        assert_equals(cache.find(request), response)

    @patch.object(Cache, '_init_paths')
    def test_find_of_nonexist_request(self, mock_cache_init_paths):
        mock_cache_init_paths.return_value = ":memory:"

        cache = Cache()
        assert_equals(cache.find("nonexist"), None)        

    @patch.object(Cache, '_init_paths')
    def test_update(self, mock_cache_init_paths):
        mock_cache_init_paths.return_value = ":memory:"

        cache = Cache()

        request = response = "foo"
        cache.add(request, response)

        for _ in range(0, 5):
            cache.update(request)

        cache._cur.execute("""SELECT t.timestamp FROM timestamp as t 
            JOIN requests as r ON t.request_id = r.id
            WHERE r.request=?""", (request,))
        assert_equals(len(cache._cur.fetchall()), 5)
