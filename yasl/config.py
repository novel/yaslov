import ConfigParser
import os.path

from yasl import exceptions as yasl_exc


class Config(object):

    # attr name, section, option, required (True/False), getter
    params = [("api_key", "api", "key", True, "get"),
              ("lang", "translation", "default_lang", False, "get"),
              ("color", "cli", "color", False, "getboolean"),
             ]

    def __init__(self, config_file):
        self._config = ConfigParser.ConfigParser()
        expanded_path = os.path.expanduser(config_file)
        parsed_files = self._config.read(expanded_path)

        if not parsed_files:
            msg = "Cannot read config file at '%s'" % (config_file,)
            raise yasl_exc.YaslConfigFileException(msg)

        self.api_key = self._config.get("api", "key")

        for param in Config.params:
            try:
                get_method = getattr(self._config, param[4])
                value = get_method(param[1], param[2])
                setattr(self, param[0], value)
            except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
                if param[3]:
                    raise
                else:
                    setattr(self, param[0], None)
