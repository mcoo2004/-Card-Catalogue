
import json

class Pokemon:
    def __init__(self, name, hp, poke_type, stage, evolves_from, attacks, ability, retreat_cost):
        self.name = name
        self.hp = hp
        self.type = poke_type
        self.stage = stage
        self.evolves_from = evolves_from
        self.attacks = attacks
        self.ability = ability
        self.retreat_cost = retreat_cost

    def __repr__(self):
        return f"{self.name} ({self.type}): {self.hp}HP"

def parse_pokemon_line_manual(line):
    fields = line.strip().split(',')
    name, hp, poke_type, stage, evolves_from, attacks_str, ability_str, retreat_cost = fields[:8]
    evolves_from = evolves_from if stage in ["Stage 1", "Stage 2"] else None
    try:
        attacks = json.loads(attacks_str.replace(''', '"')) if attacks_str else []
        ability = json.loads(ability_str.replace(''', '"')) if ability_str else {}
    except json.JSONDecodeError:
        attacks = []
        ability = {}
    retreat_cost = int(retreat_cost) if retreat_cost.isdigit() else 0
    return Pokemon(name, hp, poke_type, stage, evolves_from, attacks, ability, retreat_cost)

def load_pokemon_data_with_encoding(filename):
    pokemon_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            next(file)
            for line in file:
                if line.strip():
                    pokemon = parse_pokemon_line_manual(line)
                    pokemon_list.append(pokemon)
    except UnicodeDecodeError:  # If utf-8 fails, try ISO-8859-1. This is due to the fact that the 'e' in Pokémon is not a standard ASCII character. 
        with open(filename, 'r', encoding='ISO-8859-1') as file:
            next(file)
            for line in file:
                if line.strip():
                    pokemon = parse_pokemon_line_manual(line)
                    pokemon_list.append(pokemon)
    return pokemon_list

# Search functions and user interface remain unchanged from previous implementation

if __name__ == "__main__":
    user_interface()
