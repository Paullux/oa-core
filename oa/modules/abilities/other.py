import psutil
import random
import socket
import string

import feedparser

from oa.core import oa
from oa.core.util import  bytes2gb, switch

from oa.modules.abilities.core import info
from oa.modules.abilities.interact import say
from oa.modules.abilities.system import read_file

def diagnostics():
    """ Run system diagnostics. """
    response = 'Lancement des diagnostiques... '

    # Processor Temperature.
    if hasattr(psutil, "sondes_de_temperatures"):
        temps = psutil.sensors_temperatures()
        if not temps:
            response += "Impossible de lire la temperature.\n"
        else:
            for name, entries in temps.items():
                for entry in entries:
                    response += 'La temperature du proccesseur est actuellement de %.0f degrés centigrade...\n' %entry.current
                    break
                break

    # Memory Free.
    response += 'La memoire système est a %.0f Gigaoctet de libre...\n' %bytes2gb(oa.sys.free_memory())

    # Drive Space Free.
    response += 'Le disque dur interne est libre a %.0f Gigaoctet...\n' %bytes2gb(psutil.disk_usage('/').free)

    # Network Status.
    response += switch(is_online(), True, 'L\'accès à Internet est opérationnel.', 'Nous sommes hors-ligne.')

    say(response)


def is_online(host = '8.8.8.8', port = 53, timeout = 1):
    """ If online Return True, if not return False.
     Host: 8.8.8.8 (google-public-dns-a.google.com)
     OpenPort: 53/tcp
     Service: domain (DNS/TCP) """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        info(ex)
        return False


def random_from_file(fname):
    l = read_file(fname, result_as_list = 1)
    return random.choice(l)


def read_forecast():
    import forecastio
    """ Get the weather forecast from Dark Sky (darksky.net).
    Get your API key and longitude / latitude at: https://darksky.net/dev/
    Install 'forecastio' module with: `pip install python-forcastio` """

    # Weather For Amberg, Germany.

    api_key = "e3f8667cb539171dc2f4b389d33648ce"
    lat = 47.409342
    lng = 0.681183

    forecast = forecastio.load_forecast(api_key, lat, lng, lang='fr')
    byNow = forecast.currently()
    byHour = forecast.hourly()
    byDay = forecast.daily()
    weather_summary = """La météo actuelle est %s.\n La temperature est de %d degrés Celsius.\n %s \n %s""" %(byNow.summary, int(byNow.temperature),byHour.summary,byDay.summary)
    say(weather_summary)

def read_news_feed(news_feed, category):
    rss = feedparser.parse(news_feed)
    info(rss['feed']['title'])
    say('Lecture de l\'actualité %s.' %category)
    headline_count = 1

    # Amount of headlines to read.
    headline_amount = 5

    for post in rss.entries:
        if(headline_count == headline_amount):
            break
        else:
            headline = post.title
            exclude = set(string.punctuation)
            headline = ''.join(ch for ch in headline if ch not in exclude)
            say(headline)
            headline_count += 1

def lines_to_dict(sLines, func = lambda s : s, params = {}):
    """ Tranlate dictionary string.
      where
         end of line - separator between keys
         : - separator between key and value
         params and oa.sys dicts - is using to fill parameters:
            %(param)s, %(user)s etc
      Example string:
       key1 : value1
       key2 : value2
       ...
       You there?: yes... i am here...
       You think: i think sometimes...
    """
    params.update(oa.sys.__dict__)
    sLines = sLines %params
    ret = dict([[k, func(v)] for k, v in [[x.strip() for x in ph.split(':')] for ph in sLines.split('\n') if ph.strip() != '']])
    return ret

def say_random(slist):
    return random.choice([x.strip() for x in slist.split(',')])

def say_time():
    """ Speak the current time. """
    time = oa.sys.time_text()
    say('Il est %s.' %time)

def say_day():
    """ Speak the current day. """
    day = oa.sys.day_name()
    say('Nous sommes aujourd\'hui le %s.' %day)

def say_last_command(string = ''):
    say(string + ' ' + oa.last_command)

def get_sys(s):
    """ Return system information from `oa.sys`. """
    return getattr(oa.sys, s)
