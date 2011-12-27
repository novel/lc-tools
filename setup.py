#!/usr/bin/env python

import os
import shutil
import subprocess
import sys

from distutils.core import setup
from distutils.command.install import install
from distutils.command.sdist import sdist

VERSION = open("VERSION").read().strip()

def abspath(path):
    """A method to determine absolute path
    for a relative path inside project's directory."""

    return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), path))

PROVIDER_TOOLS_DIR = abspath("./provider_specific")
PROVIDER_TOOLS = os.listdir(PROVIDER_TOOLS_DIR)

scripts_to_install = ["lc-drivers-list",
            "lc-image-list",
            "lc-locations-list",
            "lc-node-add",
            "lc-node-do",
            "lc-node-list",
            "lc-sizes-list",
            "lb-add",
            "lb-destroy",
            "lb-list",
            "lb-member-add",
            "lb-member-list",
            "lb-member-remove",
            ]

class lc_install(install):
    user_options = install.user_options
    user_options.extend([('providertools=', None, ('List of providers for which '
        'additional tools should be included.\nSupported values: %s') % \
                ' '.join(PROVIDER_TOOLS))])

    def initialize_options(self):
        self.providertools = ' '.join(PROVIDER_TOOLS)

        install.initialize_options(self)

    def run(self):
        global scripts_to_install

        for prov_script_dir in self.providertools.split():
            try:
                scripts_to_install += [os.path.join("./provider_specific",
                    prov_script_dir, path) for path in
                    os.listdir(os.path.join(PROVIDER_TOOLS_DIR, prov_script_dir))]
            except OSError, err:
                sys.stdout.write("Problem accessing scripts for provider '%s': %s\n" % \
                        (prov_script_dir, str(err)))
                sys.exit(1)

        install.run(self)

        man_dir = abspath("./man/")

        output = subprocess.Popen([os.path.join(man_dir, "install.sh")],
                stdout=subprocess.PIPE,
                cwd=man_dir,
                env=dict({"PREFIX": self.prefix}, **dict(os.environ))).communicate()[0]
        print output


class lc_sdist(sdist):
    """We substitute default 'sdist' command to generate README file:

    README.md -> README (as github only shows *.md files as Markdown)
    """

    def run(self):
        sys.stdout.write("README.md --> README\n")
        shutil.copyfile("README.md", "README")

        sdist.run(self)

        sys.stdout.write("Cleaning up README\n")
        os.remove("README")

setup(name="lctools",
        version=VERSION,
        description="CLI tools for managing clouds, based on libcloud",
        author="Roman Bogorodskiy",
        author_email="bogorodskiy@gmail.com",
        url="http://github.com/novel/lc-tools",
        requires=["apache_libcloud (>= 0.7.1)"],
        packages=["lctools"],
        scripts=scripts_to_install,
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
