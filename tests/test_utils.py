#!/usr/bin/env python

from awkat_salet import GEO_IP_URL
from awkat_salet.utils import get_config_parser, get_country_name

def test_get_config_parser():
    """Check and read the application config file"""
    parser = get_config_parser()
    assert parser.has_section('main')


def test_get_country_name():
    """Test if get_country_name() returns the correct name of 
    the country you are.
    """
    # from local sys info
    assert get_country_name(local=True, geo_ip_url=GEO_IP_URL)
    # from a GeoIP info
    assert get_country_name(geo_ip_url=GEO_IP_URL)
