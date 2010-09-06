#!/usr/bin/env python

import subprocess
import os.path
import sys

from distutils.core import setup
from distutils.command.install import install
from distutils.command.clean import clean

class lc_install(install):

    def run(self):
        install.run(self)

        man_dir = os.path.abspath("./man/")

        output = subprocess.Popen([os.path.join(man_dir, "install.sh")],
                stdout=subprocess.PIPE, cwd=man_dir, env=dict({"PREFIX": self.prefix}, **os.environ)).communicate()[0]
        print output

setup(name="lctools",
        version="0.1.3",
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
