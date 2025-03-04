import os
import json
import random

# File to store dynamically added Pokémon
POKEMON_DATA_FILE = "pokemon_categories.json"

# Default Pokémon Categories
DEFAULT_CATEGORIES = {
    "safari": [],
    "nest": [],
    "ultra": [],
    "great": [],
    "regular": [
        "Abra", "Alakazam", "Applin", "Arrokuda", "Axew", "Barraskewda", "Bagon", 
        "Braixen", "Brionne", "Buneary", "Chimchar", "Charmander", "Charmeleon", 
        "Cinccino", "Conkeldurr", "Cryogonal", "Cutiefly", "Cyndaquil", "Dartrix", 
        "Darumaka", "Dracovish", "Dracozolt", "Dragonair", "Dratini", "Druddigon", 
        "Ducklett", "Dwebble", "Espeon", "Fennekin", "Flabebe", "Floette", "Frillish", 
        "Fraxure", "Gabite", "Gible", "Golett", "Goomy", "Grookey", "Grovyle", "Gurdurr", 
        "Hawlucha", "Heracross", "Impidimp", "Kadabra", "Lampent", "Lapras", "Litwick", 
        "Lombre", "Lopunny", "Lotad", "Magikarp", "Mankey", "Mareanie", "Mimikyu", 
        "Monferno", "Morgrem", "Morpeko", "Munchlax", "Oranguru", "Orbeetle", "Phantump", 
        "Piplup", "Porygon", "Porygon2", "Porygon-Z", "Popplio", "Prinplup", "Primarina", 
        "Primeape", "Quilava", "Rhyhorn", "Rookidee", "Rowlet", "Rufflet", "Shelgon", 
        "Shellder", "Snorlax", "Squirtle", "Staravia", "Starly", "Staryu", "Swanna", 
        "Teddiursa", "Tentacool", "Tentacruel", "Thwackey", "Timburr", "Togepi", "Togetic", 
        "Torracat", "Treecko", "Toxapex", "Trevenant", "Vikavolt", "Wartortle", "Wishiwashi", 
        "Wimpod", "Hakamo-o", "Jangmo-o", "Sirfetch'd", "Mime Jr.", "Mr. Mime"],
    "repeat": [
        "Abomasnow", "Aerodactyl", "Ampharos", "Beldum", "Beedrill", "Blacephalon", 
        "Blastoise", "Cobalion", "Cosmoem", "Cosmog", "Delphox", "Deoxys", "Dhelmise", 
        "Dialga", "Drakloak", "Duraludon", "Darmanitan", "Eternatus", "Gallade", 
        "Gardevoir", "Genesect", "Giratina", "Glastrier", "Golisopod", "Golurk", "Greninja", 
        "Groudon", "Gyarados", "Haxorus", "Ho-oh", "Hoopa", "Jellicent", "Jirachi", "Jolteon", 
        "Kartana", "Keldeo", "Kubfu", "Kyogre", "Kyurem", "Landorus", "Lapras", "Lugia", 
        "Ludicolo", "Magearna", "Marshadow", "Meloetta", "Metang", "Mewtwo", "Necrozma", 
        "Palkia", "Pheromosa", "Charizard", "Rayquaza", "Regieleki", "Regigigas", "Reshiram", 
        "Rillaboom", "Rotom", "Sceptile", "Shaymin", "Spectrier", "Starmie", "Slakoth", 
        "Terrakion", "Togekiss", "Turtonator", "Ursaring", "Venusaur", "Victini", "Vigoroth", 
        "Virizion", "Xerneas", "Yveltal", "Zacian", "Zamazenta", "Zapdos", "Zekrom", "Zeraora", 
        "Zygarde", "Arceus", "Darkrai", "Empoleon", "Goodra", "Lopunny", "Thundurus"       
    ]
}

# Load Pokémon Categories from file or use default
if os.path.exists(POKEMON_DATA_FILE):
    with open(POKEMON_DATA_FILE, "r") as f:
        POKEMON_CATEGORIES = json.load(f)
else:
    POKEMON_CATEGORIES = DEFAULT_CATEGORIES

# Function to save Pokémon categories to file
def save_pokemon_data():
    with open(POKEMON_DATA_FILE, "w") as f:
        json.dump(POKEMON_CATEGORIES, f, indent=4)

# Owner and Bot Information
OWNER_NAME = "Amit"
BOT_VERSION = "1.0"

# Command Regex Patterns
PING_COMMAND_REGEX = r'^\.ping$'
ALIVE_COMMAND_REGEX = r'^\.alive$'
HELP_COMMAND_REGEX = r'^\.help$'
EVAL_COMMAND_REGEX = r'^\.eval (.+)'
GUESSER_COMMAND_REGEX = r'^\.guess (on|off|stats)$'
HUNTER_COMMAND_REGEX = r'^\.hunt (on|off|stats)$'
LIST_COMMAND_REGEX = r'^\.list(?:\s+(\w+))?$'  # `.list <category>`
ADD_COMMAND_REGEX = r'^\.add (\w+) (\w+)$'  # `.add <pokemon> <category>`

# AFK Commands
AFK_COMMAND_REGEX = r'^\.afk(?: |$)(.*)'  # Matches `.afk` or `.afk <message>`
UNAFK_COMMAND_REGEX = r'^\.unafk$'  # Matches `.unafk`

# Timing and Limits
COOLDOWN = lambda: random.randint(3, 6)
PERIODICALLY_GUESS_SECONDS = 120
PERIODICALLY_HUNT_SECONDS = 300
HEXA_BOT_ID = 572621020

# API Credentials
API_ID = int(os.getenv('API_ID', 0))
API_HASH = os.getenv('API_HASH', "")
SESSION = os.getenv('SESSION', "")

# Chat ID
CHAT_ID = int(os.getenv('CHAT_ID', 0))

# Load Pokémon Data
with open('pokemon.json', 'r') as f:
    POKEMON = json.load(f)

__version__ = '1.0.0'
