import os

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import libcloud.security

from config import get_config

PROFILE_ENV_VAR = "LC_PROFILE"

def get_lc(profile, resource=None):
    if resource is None:
        from libcloud.compute.types import Provider
        from libcloud.compute.providers import get_driver
    else:
        pkg_name = 'libcloud.%s' % resource
        Provider = __import__(pkg_name + ".types",
                globals(), locals(), ['Provider'], -1).Provider
        get_driver =  __import__(pkg_name + ".providers",
                globals(), locals(), ['get_driver'], -1).get_driver

    if "default" == profile and PROFILE_ENV_VAR in os.environ:
        profile = os.environ[PROFILE_ENV_VAR]

    conf = get_config(profile)

    libcloud.security.VERIFY_SSL_CERT = conf.get('verify_ssl_certs') == 'true'

    extra_kwargs = {}
    extra = conf.get("extra")

    if extra != "":
        extra_kwargs = eval(extra)

        if not isinstance(extra_kwargs, dict):
            raise Exception('Extra arguments should be a Python dict')

    # a hack because libcloud driver names for Rackspace doesn't match
    # for loadbalancers and compute
    driver_name = conf.get('driver').upper()
    if 'loadbalancer' == resource and 'RACKSPACE' == driver_name:
        driver_name += "_US"

    driver = get_driver(getattr(Provider, driver_name))
    conn = driver(conf.get('access_id'), conf.get('secret_key'), **extra_kwargs)

    return conn
