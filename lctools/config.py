import stat
import os.path
import ConfigParser

LC_CONFIG = "~/.lcrc"


class MyConfig(ConfigParser.ConfigParser):
    profile = None

    def __init__(self, profile):
        self.profile = profile
        ConfigParser.ConfigParser.__init__(self,
                {"verify_ssl_certs": "false", "extra": ""})

    def get(self, option):
        return ConfigParser.ConfigParser.get(self, self.profile, option)


def get_config(profile):
    config_path = os.path.expanduser(LC_CONFIG)

    if os.stat(config_path)[stat.ST_MODE] & \
            (stat.S_IRWXG | stat.S_IRWXO) != 0:
        raise RuntimeError("%s: permissions are too loose, set to 600" % \
                LC_CONFIG)

    conf = MyConfig(profile)
    conf.read(os.path.expanduser(config_path))

    return conf
