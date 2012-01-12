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
