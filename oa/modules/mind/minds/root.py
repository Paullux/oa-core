from oa.core.util import command_registry

from oa.modules.abilities.interact import say, play, mind
from oa.modules.abilities.other import read_news_feed, diagnostics, read_forecast
from oa.modules.abilities.other import say_day, say_last_command, say_time
import webbrowser

kws = {}

command = command_registry(kws)

@command("démarre cerveau")
def hello_world():
     say('Salut tout le Monde')

@command("ferme assistant")
def close_assistant():
    play('beep_close.wav')
    mind('boot')

@command(["liste commandes", "que dire"])
def list_commands():
    say('Les commandes vocales disponibles sont:\n{}'.format(',\n'.join(kws.keys())))

@command("nouvelles du jour")
def read_world_news():
    read_news_feed('https://www.lemonde.fr/rss/une.xml', 'la une du monde')

@command("lance diagnostiques")
def run_diagnostics():
    diagnostics()

@command("chante une chanson")
def sing_a_song():
    webbrowser.open('https://www.youtube.com/watch?v=6PeRPLtnnOM')
    #play('ToutVaBien.wav')

@command("quel jour sommes nous")
def what_day():
    say_day()

@command("qu'est-ce que j'ai dit")
def what_command():
    say_last_command('Vous avez dit:')

@command("donne la Météo")
def what_weather():
    read_forecast()

@command("quelle heure est-il")
def what_time():
    say_time()

@command("lance Internet")
def launch_internet():
    webbrowser.open_new_tab('https://www.qwant.com/?l=fr')
    
@command("lance Mail")
def open_mail():
    webbrowser.open('mailto:', new=1)
