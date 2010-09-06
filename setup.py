#!/usr/bin/env python

import os
import shutil
import subprocess
import sys

from distutils.core import setup
from distutils.command.install import install
from distutils.command.sdist import sdist

class lc_install(install):

    def run(self):
        install.run(self)

        man_dir = os.path.abspath("./man/")

        output = subprocess.Popen([os.path.join(man_dir, "install.sh")],
                stdout=subprocess.PIPE,
                cwd=man_dir,
                env=dict({"PREFIX": self.prefix}, **os.environ)).communicate()[0]
        print output

class lc_sdist(sdist):
    """We substitute default 'sdist' command for the sake of two things:

    * README.md -> README (as github only shows *.md files as Markdown
    """

    def run(self):
        sys.stdout.write("README.md --> README\n")
        shutil.copyfile("README.md", "README")
        
        sdist.run(self)
        
        sys.stdout.write("Cleaning up README\n")
        os.remove("README")

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
        cmdclass={"install": lc_install, "sdist": lc_sdist},)
