import os
import stat

from nose.tools import *

from lctools import config

class TestConfig(object):
    test_filename = "bebebe"

    def setup(self):
        fd = open(self.test_filename, 'w')
        fd.write("[default]\n")
        fd.write("foo = bar\n")
        fd.close()
        os.chmod(self.test_filename, stat.S_IRUSR)

    def test_basic_functionality(self):
        config.LC_CONFIG = self.test_filename
        conf = config.get_config("default")
        assert_true("default" in conf.sections())
        assert_equal(conf.get("foo"), "bar")

    @raises(RuntimeError)
    def test_get_config_permission_checks(self):
        os.chmod(self.test_filename, stat.S_IRWXG | stat.S_IRWXO)
        config.LC_CONFIG = self.test_filename
        config.get_config("default")

    def test_defaults(self):
        config.LC_CONFIG = self.test_filename
        conf = config.get_config("default")
        print conf.get("verify_ssl_certs")

    def teardown(self):
        os.unlink(self.test_filename)
