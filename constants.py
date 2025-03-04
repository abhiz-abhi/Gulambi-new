import os
import json
import random

# Pokémon Categories
SAFARI = set([])
NEST_BALL = set([])
ULTRA_BALL = set([])
GREAT_BALL = set([])
REGULAR_BALL = set([
"Abra", "Alakazam", "Buneary", "Cyndaquil", "Dartrix", "Espeon",
"Gabite", "Gible", "Goomy", "Jolteon", "Kadabra", "Kleavor",
"Lilligant", "Lopunny", "Munchlax", "Porygon", "Porygon2", "Porygon-Z",
"Quilava", "Rotom", "Rowlet", "Rufflet", "Sliggoo", "Snorlax",
"Staravia","Starly", "Teddiursa", "Voltorb", "Wyrdeer", "Zorua",
"Applin", "Arrokuda", "Axew", "Barraskewda", "Bagon", "Braixen",
"Brionne", "Chimchar", "Charmander", "Charmeleon", "Cinccino", "Conkeldurr",
"Cryogonal", "Cutiefly", "Darumaka", "Dracovish", "Dracozolt", "Dragonair",
"Dratini", "Druddigon", "Ducklett", "Dwebble", "Fennekin", "Flabebe", "Floette",
"Frillish", "Fraxure", "Golett", "Grookey", "Grovyle", "Gurdurr",
"Hawlucha", "Heracross", "Impidimp", "Lampent", "Lapras", "Litwick",
"Lombre", "Lotad", "Magikarp", "Mankey", "Mareanie", "Mimikyu",
"Monferno", "Morgrem", "Morpeko", "Oranguru", "Orbeetle", "Phantump",
"Piplup", "Popplio", "Prinplup", "Primarina", "Primeape", "Rhyhorn",
"Rookidee", "Shelgon", "Shellder", "Squirtle", "Staryu", "Swanna",
"Tentacool", "Tentacruel", "Thwackey", "Timburr", "Togepi", "Togetic",
"Torracat", "Treecko", "Toxapex", "Trevenant", "Vikavolt", "Wartortle",
"Wishiwashi", "Wimpod", "Hakamo-o", "Jangmo-o", "Sirfetch'd", "Mime Jr.", "Mr. Mime"
])

REPEAT_BALL = set(
"Abomasnow", "Aerodactyl", "Ampharos", "Beldum", "Beedrill", "Blacephalon",
"Blastoise", "Cobalion", "Cosmoem", "Cosmog", "Delphox", "Deoxys",
"Dhelmise", "Abomasnow", "Arceus", "Darkrai", "Dialga", "Empoleon",
"Gallade", "Gardevoir", "Giratina", "Goodra", "Gyarados", "Landorus",
"Lopunny", "Palkia", "Regigigas", "Shaymin", "Thundurus",
"Togekiss", "Dialga", "Drakloak", "Duraludon", "Darmanitan", "Eternatus",
"Gallade", "Gardevoir", "Genesect", "Giratina", "Glastrier", "Golisopod",
"Golurk", "Greninja", "Groudon", "Gyarados", "Haxorus", "Ho-oh",
"Hoopa", "Jellicent", "Jirachi", "Jolteon", "Kartana", "Keldeo",
"Kubfu", "Kyogre", "Kyurem", "Landorus", "Lapras", "Lugia", "Ludicolo",
"Magearna", "Marshadow", "Meloetta", "Metang", "Mewtwo", "Necrozma",
"Palkia", "Pheromosa", "Charizard", "Rayquaza", "Regieleki", "Regigigas",
"Reshiram", "Rillaboom", "Rotom", "Sceptile", "Shaymin", "Spectrier",
"Starmie", "Slakoth", "Terrakion", "Togekiss", "Turtonator", "Ursaring",
"Venusaur", "Victini", "Vigoroth", "Virizion", "Xerneas", "Yveltal",
"Zacian", "Zamazenta", "Zapdos", "Zekrom", "Zeraora", "Zygarde"
])

# Owner and Bot Information
OWNER_NAME = "Amit"
BOT_VERSION = "1.0"

# Commands
PING_COMMAND_REGEX = r'^\.ping$'
ALIVE_COMMAND_REGEX = r'^\.alive$'
HELP_COMMAND_REGEX = r'^\.help$'
EVAL_COMMAND_REGEX = r'^\.eval (.+)'
GUESSER_COMMAND_REGEX = r'^\.guess (on|off|stats)$'
HUNTER_COMMAND_REGEX = r'^\.hunt (on|off|stats)$'
LIST_COMMAND_REGEX = r'^\.list(?:\s+(\w+))?$'  # Now supports .list <category>

# AFK Commands
AFK_COMMAND_REGEX = r'^\.afk(?: |$)(.*)'  # Matches .afk or .afk <message>
UNAFK_COMMAND_REGEX = r'^\.unafk$'  # Matches .unafk

# Timing and Limits
COOLDOWN = lambda: random.randint(3, 6)
PERIODICALLY_GUESS_SECONDS = 120
PERIODICALLY_HUNT_SECONDS = 300
HEXA_BOT_ID = 572621020

# API Credentials
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION = os.getenv('SESSION')

# Chat ID
CHAT_ID = int(os.getenv('CHAT_ID'))

# Load Pokémon Data
with open('pokemon.json', 'r') as f:
    POKEMON = json.load(f)

version = '1.0.0'
