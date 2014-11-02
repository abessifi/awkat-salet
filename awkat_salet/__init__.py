#!/usr/bin/env python

"""Package for awkat_salet."""

__project__ = 'awkat_salet'
__version__ = '0.0.0'
VERSION = __project__ + '-' + __version__

from utils import get_config_parser

# Parse the application config file
parser = get_config_parser()
COUNTRY = parser.get('main', 'country')
GEO_IP_URL = parser.get('main', 'geo_ip_api')
MUSLIMSALAT_API_URL = parser.get('muslimsalat-api', 'url')
