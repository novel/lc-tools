import os.path
import ConfigParser

LC_CONFIG = "~/.lcrc"


class MyConfig(ConfigParser.ConfigParser):
    profile = None

    def __init__(self, profile):
        self.profile = profile
        ConfigParser.ConfigParser.__init__(self)

    def get(self, option):
        return ConfigParser.ConfigParser.get(self, self.profile, option)


def get_config(profile):
    conf = MyConfig(profile)
    conf.read(os.path.expanduser(LC_CONFIG))

    return conf
