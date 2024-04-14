import json


class PokemonCard:
  # Initialize Pokemon card with attributes
  def __init__(self, name, hp, card_type, stage, evolves_from, attacks,
               ability, retreat_cost):
    self.name = name
    self.hp = int(hp)
    self.card_type = card_type
    self.stage = stage
    self.evolves_from = evolves_from
    self.attacks = attacks
    self.ability = ability
    self.retreat_cost = int(retreat_cost)

  # String representation. makes it display a lot nicer, breaks line for each attribute (if it exists)
  def __repr__(self):
    repr_str = f"Pokemon Card Details:\n"
    repr_str += f"Name: {self.name}\n"
    repr_str += f"HP: {self.hp}\n"
    repr_str += f"Type: {self.card_type}\n"
    repr_str += f"Stage: {self.stage}\n"
    if self.evolves_from:
      repr_str += f"Evolves From: {self.evolves_from}\n"
    repr_str += "Attacks:\n"
    for attack in self.attacks:
      repr_str += f"\tName: {attack['Name']}\n"
      repr_str += f"\tDescription: {attack['Description']}\n"
      repr_str += f"\tEnergy Types: {', '.join(attack['Energy'].keys())}\n"
      repr_str += f"\tDamage: {attack['Damage']}\n"
    if self.ability:
      repr_str += "Ability:\n"
      repr_str += f"\tName: {self.ability['Name']}\n"
      repr_str += f"\tDescription: {self.ability['Description']}\n"
    repr_str += f"Retreat Cost: {self.retreat_cost}\n"
    return repr_str


class CardCollection: # Collection of Pokemon cards
  # Manage card collection
  def __init__(self):
    self.cards = []

  # Add card to collection
  def add_card(self, card):
    self.cards.append(card)

  # Find cards by type
  def find_by_type(self, type):
    return [
        card for card in self.cards if card.card_type.lower() == type.lower()
    ]

  # Find by attack damage
  def find_by_attack_damage(self, minimum_damage):
    result = []
    for card in self.cards:
      for attack in card.attacks:
        damage = parse_damage(attack['Damage'])
        if damage >= minimum_damage:
          result.append(card)
          break
    return result

  # Find by HP
  def find_by_hp(self, hp):
    return [card for card in self.cards if card.hp >= hp]

  # Find by ability

  def find_by_ability(self, ability_name):
    return [
        card for card in self.cards if card.ability
        and card.ability['Name'].lower() == ability_name.lower()
    ]

  # Find by stage
  def find_by_stage(self, stage):
    return [card for card in self.cards if card.stage.lower() == stage.lower()]

  # Find by energy requirement
  def find_by_energy_requirement(self, energy_type, amount):
    result = []
    for card in self.cards:
      for attack in card.attacks:
        energy_requirements = attack.get('Energy', {})
        if energy_requirements.get(energy_type, 0) >= amount:
          result.append(card)
          break
    return result


# Parse damage value
def parse_damage(damage_str):
  filtered_damage = ''.join(
      filter(lambda x: x.isdigit() or x == '+', damage_str))
  if '+' in filtered_damage:
    return int(filtered_damage.split('+')[0])
  return int(filtered_damage) if filtered_damage.isdigit() else 0


# Load cards from JSON
def load_cards_from_json(file_path):
  with open(file_path, 'r') as file:
    data = json.load(file)
    card_collection = CardCollection()
    for key, item in data.items():
      card = PokemonCard(name=item['Name'],
                         hp=item['HP'],
                         card_type=item['Type'],
                         stage=item['Stage'],
                         evolves_from=item.get('EvolvesFrom', None),
                         attacks=item['Attacks'],
                         ability=item.get('Ability', None),
                         retreat_cost=item['RetreatCost'])
      card_collection.add_card(card)
    return card_collection


# Display card details
def display_cards(cards):
  if not cards:
    print("No cards found.")
  else:
    for card in cards:
      print(card)
      print("-" * 40)


# Run CLI
def run_cli():
  filename = input("Enter the filename of the Pokemon card data: ")
  collection = load_cards_from_json(filename)
  while True:
    print("\nMenu:")
    print("1. Search by Type")
    print("2. Search by Attack Damage")
    print("3. Search by HP")
    print("4. Search by Ability")
    print("5. Search by Stage")
    print("6. Search by Energy Requirement")
    print("7. Exit")
    choice = input("Choose an option (1-7): ")

    if choice == '1':
      cards = collection.find_by_type(
          input("Enter the Pokemon type to search: "))
      display_cards(cards)
    elif choice == '2':
      cards = collection.find_by_attack_damage(
          int(input("Enter the minimum attack damage to search for: ")))
      display_cards(cards)
    elif choice == '3':
      cards = collection.find_by_hp(
          int(input("Enter the HP amount to search for: ")))
      display_cards(cards)
    elif choice == '4':
      cards = collection.find_by_ability(
          input("Enter the ability name to search for: "))
      display_cards(cards)
    elif choice == '5':
      cards = collection.find_by_stage(
          input("Enter the stage to search for: "))
      display_cards(cards)
    elif choice == '6':
      energy_type = input(
          "Enter the energy type to search for(case sensitive): ")
      amount = int(
          input("Enter the minimum amount of this energy type required: "))
      cards = collection.find_by_energy_requirement(energy_type, amount)
      display_cards(cards)
    elif choice == '7':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
  run_cli()
