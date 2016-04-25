import ConfigParser
import os.path


class Config(object):

    def __init__(self, config_file):
        self._config = ConfigParser.ConfigParser()
        self._config.read(os.path.expanduser(config_file))

        self.api_key = self._config.get("api", "key")
        try:
            self.lang = self._config.get("translation", "default_lang")
        except ConfigParser.NoOptionError:
            self.lang = None
