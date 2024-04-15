# -Card-Catalogue
Pokémon Card Catalogue

Overview:
This Python program enables users to store information about Pokémon cards in a searchable catalogue. By reading data from a JSON file, users can input details about each Pokémon card, including characteristics like Name, HP, Type, and more. The program allows for searches based on various criteria such as Pokémon Type, Attack Damage, HP, Abilities, and others.

Features:
Load Pokémon card data from a JSON file.
Store detailed information on Pokémon cards, excluding Trainer cards.
Search functionality for finding Pokémon based on Type, Attack Damage, HP, Abilities, Stage of Evolution, and required Energy types for attacks.
Interactive command-line interface for user input and queries.

Requirements:
Python 3.9 or higher (as per the rubric, ensuring compatibility with Python 3.9 on Windows)
No third-party libraries are used, adhering to the assignment's stipulation of using only standard libraries.

Getting Started:
Ensure you have Python 3.9 or higher installed on your system.
Download updated_program2.py and pokemon_card_list.JSON to the same directory.
Open a command-line interface (CLI) and navigate to the directory containing the downloaded files.

Usage:
To run the program, execute the following command in your CLI:

"python updated_program2.py"

Upon launch, the program will prompt you to enter the name of the input file (pokemon_card_list.JSON). Once the data is loaded, you will be presented with an interactive menu that guides you through the various search options available. Follow the on-screen instructions to search for Pokémon cards based on your criteria of interest.

Input File Format:
The program accepts data through a JSON file named pokemon_card_list.JSON. This file should include the following information for each Pokémon card:

Name
HP
Type (e.g., Grass, Fire, Lightning)
Stage (Basic, Stage 1, Stage 2)
Evolves From (for Stage 1 and Stage 2 Pokémon)
Attacks (including Name, Description, Energy types required, Type, Number, Damage)
Ability (Name, Description)
Retreat Cost
Duplicate entries in the file can be handled based on your preference: either ignore duplicates or store both.



License:
This project is open-source and available under the MIT License.
