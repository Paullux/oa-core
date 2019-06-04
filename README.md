# Open Assistant

Il s'agit d'un assistant vocale open source en cours de développement. Pour vous permettre de créer vous-même votre AI !

Open Assistant est un assistant personnel privé et open source, il est personnalisable pour obtenir un système d'exploitation utilisable uniquement par des commandes vocales.

Mon but est la traduction en français du projet et d'ajouter de nouvelles commandes vocales afin d'avoir un système complet.
Le projet original en anglais est disponible à l'adresse suivante [Open Assistant](http://openassistant.org/)

# Installation

requirements.txt est disponible dans le dépôt.

## Ubuntu Linux

* Installer les paquets nécéssaires suivants : ``sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev espeak libttspico-utils``
* Installer les dépendances Python : `pip install -r requirements.txt`

## Arch Linux

* Installer les paquets nécéssaires suivants : ``trizen -S swig espeak pico-tts svox-pico-bin`` ou ``yaourt -S swig espeak pico-tts svox-pico-bin``
* Installer les dépendances Python : `pip install -r requirements.txt`

# Pour utiliser Open Assistant

* [Téléchargez Open Assistant](https://github.com/Paullux/oa-core/archive/master.zip)
* Lancer Open Assistant dans le dossier dézippé, issue du téléchargement : ``python -m oa``
* Vérifier que votre microphone est opérationnel et que les différents niveaux sonores sont correctement réglés.
* Dîtes "Démarre Cerveau !" pour le test d'écoute. Si vous entendez R2D2, le cerveau "boot" vous entend.
* Dîtes "Lance Assistant !" pour lancer le cerveau "root". Dîte "Démarre Cerveau !" et vous entenderez la réponse, "Salut tout le monde !"
* Dîtes "Liste commandes !" pour obtenir la liste des commandes vocales disponibles.
* Ajouter les vôtres !
