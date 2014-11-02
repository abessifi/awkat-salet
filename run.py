#!/usr/bin/env python

from awkat_salet import GEO_IP_URL
from awkat_salet.utils import get_country_name

if __name__ == '__main__':
    print get_country_name(geo_ip_url=GEO_IP_URL)
