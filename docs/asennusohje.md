# Asennusohje/jatkokehitysohje

Sovellus on verkossa toimiva, joten käyttäjän ei tarvitse asentaa sitä paikallisesti koneelleen käyttäkseen sitä.

Jos käyttäjä haluaa jatko kehittää sovellusta, niin käyttäjän tulee

1. Ladata git projektin koneelleensa

`git clone https://github.com/HegePI/tsoha-2020-projekti-dnd-register.git`

2. Luoda virtuaaliympäristö proketin sisään

`python -m venv venv`

3. Aktivoida virtuaaliympäristö

`source venv/bin/activate`

4. Asentaa riippuvuudet

`pip install -r requirements.txt`

Nyt käyttäjä voi käynnistää sovelukksen lokaalisti komennolla

`python run.py`


Käyttäjä voi luoda uudesta toiminnallisuudesta pull requestin seuraamalla ohjeita @ [https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)