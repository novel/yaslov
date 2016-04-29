import ConfigParser
import os.path

from yasl import exceptions as yasl_exc


class Config(object):

    def __init__(self, config_file):
        self._config = ConfigParser.ConfigParser()
        expanded_path = os.path.expanduser(config_file)
        parsed_files = self._config.read(expanded_path)

        if not parsed_files:
            msg = "Cannot read config file at '%s'" % (config_file,)
            raise yasl_exc.YaslConfigFileException(msg)

        self.api_key = self._config.get("api", "key")
        try:
            self.lang = self._config.get("translation", "default_lang")
        except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
            self.lang = None
