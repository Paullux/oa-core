from oa.core import oa
from oa.core.util import command_registry

from oa.modules.abilities.interact import say, play, mind


kws = {}
command = command_registry(kws)

@command("démarre cerveau")
def response_sound():
  play('r2d2.wav')

@command("lance assistant")
def open_root():
  play('beep_open.wav')
  mind('root')

@command(["liste commandes", "aide"])
def list_commands():
    say('Les commandes vocales sont les suivantes:..')
    [say(cmd) for cmd in kws.keys()]

@command("stop écoute")
def do_exit():
    play('silence.wav')
    oa.core.finished.set()
