from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import libcloud.security

from config import get_config


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

    conf = get_config(profile)

    libcloud.security.VERIFY_SSL_CERT = conf.get('verify_ssl_certs') == 'true'

    driver = get_driver(getattr(Provider, conf.get('driver').upper()))
    conn = driver(conf.get('access_id'), conf.get('secret_key'))

    return conn
