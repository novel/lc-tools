"""Test package"""

import os.path
import sys

def setup_package():
    # insert top-level dir to python path
    # so we could easily import stuff from
    # tests
    sys.path.insert(0, os.path.abspath("../"))
