try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="lctools",
        version="0.1.0",
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
            "lc-sizes-list"]
)
