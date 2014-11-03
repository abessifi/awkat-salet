import os
import requests
from ConfigParser import ConfigParser

class ConfigFileNotFound(Exception): pass
class APIUrlNotDefined(Exception): pass

def get_config_parser(path=''):
    """Locate the application config file
    Parameters:
        path - Path to a givin config file
    Returns:
        returns a ConfigParser object
    """
    parser = ConfigParser()
    if os.path.exists(path):
        return parser.read(path)
    print("[WARN] '%s' doesn't exist. Looking somewhere.." % path)
    for location in os.curdir, os.path.expanduser('~'), '/etc/awkat_salet', \
                    os.environ.get('AWKAT_SALET_CONF'):
        try:
            with open(os.path.join(location, 'awkat_salet.conf')) as f:
                parser.readfp(f)
            print("[INFO] Use configuration file in %s/" % location)
            return parser
        except IOError:
            pass
    raise ConfigFileNOtFound("No configuration file found !")

def get_country_name(local=False, geo_ip_url=''):
    """Determine the country name either from system information or from
    IP Geolocation. Note that local sys info and GeoIP may be different.
    Parameters:
        local - check or not in local system infos
    Returns:
        returns the country name.
    """
    country = ''
    if local: # Get location from local system info
        timezone_file = '/etc/timezone' # In Linux OSs
        try:
            with open(timezone_file, 'r') as f:
                content = f.read().split()
            return content[0].split('/')[1].lower()
        except IOError:
            print("[ERROR] '%s' not found !" % timezone_file)
            return country
    # Else, get country name from an GeoIP API.
    if not geo_ip_url: raise APIUrlNotDefined("GeoIP API URL not defined.")
    try:
        response = requests.get(geo_ip_url)
        country = response.json()['timezone'].split('/')[1].lower()
    except requests.HTTPError:
        print("[ERROR] Please check the API url.")
    except requests.ConnectionError:
        print("[ERROR] Connection aborted. Please make sure you're connect.")
    except Exception as e:
        print("[ERROR] Unexpected error ! %s" % e)
    return country
