#!/usr/bin/env python

import subprocess
import os.path
import sys

from distutils.core import setup
from distutils.command.install import install
from distutils.command.clean import clean

class lc_install(install):

    def run(self):
#        install.run(self)

#        print "HERE WE GO"
#        print self.dump_options()
#        print self.prefix
#        sys.exit(0)

        man_dir = os.path.abspath("./man/")

        output = subprocess.Popen([os.path.join(man_dir, "install.sh")],
                stdout=subprocess.PIPE, cwd=man_dir, env=dict({"PREFIX": self.prefix}, **os.environ)).communicate()[0]
        print output

#class lc_clean(clean):
#
#    def run(self):
#        clean.run(self)
#
#        print "STUFFF YZ CLEAN!!"


setup(name="lctools",
        version="0.1.2",
        description="CLI tools for managing clouds, based on libcloud",
        author="Roman Bogorodskiy",
        author_email="bogorodskiy@gmail.com",
        url="http://github.com/novel/lc-tools",
        packages=["lctools"],
        scripts=["lc-drivers-list",
            "lc-image-list",
            "lc-node-add",
            "lc-node-do",
            "lc-node-list",
            "lc-sizes-list"],
        license='Apache License (2.0)',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: System'],
        cmdclass={"install": lc_install},)
