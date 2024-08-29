from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Define the available options
classAndSubclass = {
    "Class": [
        "Artificer", "Artificer", "Artificer", "Artificer",
        "Barbarian", "Barbarian", "Barbarian", "Barbarian", "Barbarian", "Barbarian", "Barbarian", "Barbarian",
        "Bard", "Bard", "Bard", "Bard", "Bard", "Bard", "Bard", "Bard",
        "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric", "Cleric",
        "Druid", "Druid", "Druid", "Druid", "Druid", "Druid", "Druid",
        "Fighter", "Fighter", "Fighter", "Fighter", "Fighter", "Fighter", "Fighter", "Fighter", "Fighter", "Fighter",
        "Monk", "Monk", "Monk", "Monk", "Monk", "Monk", "Monk", "Monk", "Monk", "Monk",
        "Paladin", "Paladin", "Paladin", "Paladin", "Paladin", "Paladin", "Paladin", "Paladin", "Paladin",
        "Ranger", "Ranger", "Ranger", "Ranger", "Ranger", "Ranger", "Ranger", "Ranger",
        "Rogue", "Rogue", "Rogue", "Rogue", "Rogue", "Rogue", "Rogue", "Rogue", "Rogue", 
        "Sorcerer", "Sorcerer", "Sorcerer", "Sorcerer", "Sorcerer", "Sorcerer", "Sorcerer",
        "Warlock", "Warlock", "Warlock", "Warlock", "Warlock", "Warlock", "Warlock", "Warlock", "Warlock",
        "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard", "Wizard"
    ],
    "Subclass": [
        "Armorer", "Alchemist", "Artillerist", "Battle Smith",
        "Path of the Berserker", "Path of the Totem Warrior", "Path of the Ancestral Guardian", "Path of the Storm Herald", "Path of the Zealot", "Path of the Beast", "Path of the Wild Soul", "Path of the Battlerager",
        "College of Lore", "College of Valor", "College of Creation", "College of Glamor", "College of Swords", "College of Whispers", "College of Eloquence", "College of Spirits",
        "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain", "War Domain", "Death Domain", "Twilight Domain", "Order Domain", "Forge Domain", "Grave Domain", "Peace Domain", "Arcane Domain",
        "Circle of the Land", "Circle of the Moon", "Circle of Dreams", "Circle of the Shepherd", "Circle of Spores", "Circle of Stars", "Circle of Wildfire",
        "Champion", "Battle Master", "Eldritch Knight", "Arcane Archer", "Cavalier", "Samurai", "Psi Warrior", "Rune Knight", "Echo Fighter", "Purple Dragon Knight",
        "Way of the Open Hand", "Way of the Shadow", "Way of the Four Elements", "Way of Mercy", "Way of the Astral Self", "Way of the Drunken Master", "Way of the Kensei", "Way of the Sun Soul", "Way of Long Death", "Way of the Ascendant Dragon",
        "Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance", "Oathbreaker", "Oath of Conquest", "Oath of Redemption", "Oath of Glory", "Oath of the Watchers", "Oath of the Crown",
        "Fey Wanderer", "Swarmkeeper", "Gloom Stalker", "Horizon Walker", "Monster Slayer", "Hunter", "Beast Master", "Drakewarden",
        "Thief", "Assassin", "Arcane Trickster", "Inquisitive", "Mastermind", "Scout", "Swashbuckler", "Phantom", "Soulknife",
        "Aberrant Mind", "Clockwork Soul", "Divine Soul", "Shadow Magic", "Storm Sorcery", "Draconic Bloodline", "Wild Magic",
        "The Archfey", "The Fiend", "The Great Old One", "The Celestial", "Undying", "The Hexblade", "The Fathomless", "The Genie", "The Undead",
        "School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Necromancy", "School of Transmutation", "School of Graviturgy", "School of Chronurgy", "War Magic", "Bladesinging", "Order of Scribes"
    ]
}

df_classesAndSubclasses = pd.DataFrame(classAndSubclass)

@app.route('/process', methods=['POST'])

# Implement character generation logic here
def generate_character():
    characterClass, subclass = chooseRandomClassAndSubclass(df_classesAndSubclasses)

    character = {
        "class": characterClass,
        "subclass": subclass,
    }
    return character

def chooseRandomClassAndSubclass(df_classesAndSubclasses):
    chosenClass = df_classesAndSubclasses.sample(1)
    characterClass = chosenClass.iloc[0]['Class']
    subclass = chosenClass.iloc[0]['Subclass']
    return characterClass, subclass

    # # placeholder for actual character generation
    # return "Python-generated character"

if __name__ == '__main__':
    app.run(port=5001)