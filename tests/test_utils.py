#!/usr/bin/env python

from awkat_salet import GEO_IP_URL
from awkat_salet.utils import get_config_parser, get_country_name, \
     APIUrlNotDefined
import pytest

def test_get_config_parser():
    """Check and read the application config file"""
    parser = get_config_parser()
    assert parser.has_section('main')

def test_get_country_name():
    """Test if get_country_name() returns the correct name of 
    the country you are.
    """
    # from local sys info
    assert get_country_name(local=True)
    # from a GeoIP info
    assert get_country_name(geo_ip_url=GEO_IP_URL)
    with pytest.raises(APIUrlNotDefined) as e:
        get_country_name()
    assert e.value.message == "GeoIP API URL not defined."

def test_get_prayer_times():
    """Check if we get prayer times from the API
    regarding the country location
    """
    pass
