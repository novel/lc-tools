from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import libcloud.security

from config import get_config


def get_lc(profile):
    conf = get_config(profile)

    libcloud.security.VERIFY_SSL_CERT = conf.get('verify_ssl_certs') == 'true'

    extra_kwargs = {}
    extra = conf.get("extra")

    if extra != "":
        extra_kwargs = eval(extra)

        if not isinstance(extra_kwargs, dict):
            raise Exception('Extra arguments should be a Python dict')

    driver = get_driver(getattr(Provider, conf.get('driver').upper()))
    conn = driver(conf.get('access_id'), conf.get('secret_key'), **extra_kwargs)

    return conn
