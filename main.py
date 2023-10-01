from rdflib import Graph, RDF, URIRef

def load_ontology():
    g = Graph()
    g.parse("my_file.rdf", format="xml")
    individuals = {}

    for s, p, o in g.triples((None, RDF.type, None)):
        if str(o) == "http://www.w3.org/2002/07/owl#NamedIndividual":
            continue

        individual_name = str(s).split("#")[-1]
        class_name = str(o).split("#")[-1]

        if individual_name not in individuals:
            individuals[individual_name] = []
        individuals[individual_name].append(class_name)

    return individuals

def get_user_preferences():
    questions = {
        'Genre': ['Roguelike', 'Fighting', 'Platformer', 'Racing', 'MMO', 'RPG', 'BattleRoyale', 'Puzzle', 'Tactical', 'Card', 'Build', 'Strategy', 'Survival', 'Action', 'VR', 'Horror', 'Sandbox', 'Stealth', 'Arcade', 'Simulation', 'Sports', 'OpenWorld', 'Adventure', 'MOBA'],
        'Game_for': ['girls', 'boys'],
        'AgeRating': ['Adults_Only_18+', 'Mature', 'Teen', 'Early_childhood', 'Everyone_10_and_older', 'Everyone'],
        'Raring_Metacritic': ['100-90', '90-70', '70-0']
    }

    user_preferences = {}
    for question, options in questions.items():
        print(f"{question}:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        choice = int(input("Choose one: "))
        user_preferences[question] = options[choice-1]

    return user_preferences

def recommend_game(individuals, user_preferences):
    for individual, classes in individuals.items():
        if 'Game' in classes:
            if all(pref in classes for pref in user_preferences.values()):
                return individual
    return "No suitable game found."

if __name__ == "__main__":
    individuals = load_ontology()
    user_preferences = get_user_preferences()
    recommended_game = recommend_game(individuals, user_preferences)
    print(f"Recommended game: {recommended_game}")