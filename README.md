# MarocDocs - TP n°3 TeamCity & SAST  TYD


Projet pédagogique pour un pipeline DevSecOps simple :
Tests Python -> scan SAST Bandit -> packaging des sources.

## Préparation

Sur une VM Ubuntu Build Agent, installer Bandit dans un environnement virtuel
accessible au compte du service agent, par exemple :

    sudo apt-get update
    sudo apt-get install -y python3 python3-venv python3-pip git
    sudo install -d -m 755 /opt/teamcity-tools
    sudo python3 -m venv /opt/teamcity-tools/bandit-venv
    sudo /opt/teamcity-tools/bandit-venv/bin/python -m pip install 'bandit==1.9.4'

## Tester localement

    python3 -m unittest discover -s tests -v
    /opt/teamcity-tools/bandit-venv/bin/bandit -r app -ll -ii

Le scan doit échouer au départ car `app/portal.py` utilise `shell=True`.
Cette vulnérabilité est volontaire, réservée au laboratoire. Ne pas déployer.

## Corriger

    cp corrections/portal_corrige.py app/portal.py
    python3 -m unittest discover -s tests -v
    /opt/teamcity-tools/bandit-venv/bin/bandit -r app -ll -ii

Le scan doit maintenant réussir : la version corrigée utilise pathlib.

Voir le guide Word/PDF fourni pour la configuration TeamCity, les trois Build
Steps, le dépôt Git, les Artifacts et les cas de diagnostic.

## Fichiers pratiques supplémentaires

- `TEAMCITY_ETAPES_A_COPIER.txt` : les trois scripts à coller dans l'interface TeamCity.
- `EXEMPLES_OUTPUTS.txt` : sorties indicatives FAILED puis SUCCESS (non issues d'un build réel).
- `scenarios/portal_vulnerable.py` : version d'origine pour rejouer l'incident.
