from nose.tools import *

import yasl.utils


class TestUtils(object):

    def test_htmlunscape_string_with_quot(self):
        input_string = "hello &quot;world&quot;!"
        expected_output_string = 'hello "world"!'

        assert_equal(yasl.utils.htmlunescape(input_string),
                expected_output_string)
