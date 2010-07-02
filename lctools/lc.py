from libcloud.types import Provider
from libcloud.providers import get_driver

from config import get_config

def get_lc(profile):
    conf = get_config(profile)

    driver = get_driver(getattr(Provider, conf.get('driver').upper()))
    conn = driver(conf.get('access_id'), conf.get('secret_key'))

    return conn
