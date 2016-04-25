import os.path
from xml.sax.saxutils import unescape as xunescape

from xdg import BaseDirectory


def htmlunescape(string):
    return xunescape(string, entities={'&quot;': '"'})


def default_config_path():
    return os.path.join(BaseDirectory.xdg_config_home,
                        '.yaslov.conf')


def cache_dir():
    return os.path.join(BaseDirectory.xdg_cache_home,
                        "yaslov")
