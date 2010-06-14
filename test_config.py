import os

from nose.tools import *

import config

class config_test(object):
    test_filename = "bebebe"

    def setup(self):
        fd = open(self.test_filename, 'w')
        fd.write("[default]\n")
        fd.write("foo = bar\n")
        fd.close()

    def test_basic_functionality(self):
        config.LC_CONFIG = self.test_filename
        conf = config.get_config("default")
        assert_true("default" in conf.sections())
        assert_equal(conf.get("foo"), "bar")

    def teardown(self):
        os.unlink(self.test_filename)
