from flask import Flask, abort, request
from flask import jsonify

app = Flask(__name__)

# Données simulées d'une API
pokemon_db = [
    {"id" : 1, "name" : "Bulbizarre", "type" : "plante, poison", "faiblesses" : "feu, vol, glace, psy" ,"categorie" : "graine", "taille" : 0.7, "poids" : 6.9},
    {"id" : 4, "name" : "Salamèche", "type" : "feu", "faiblesses" : "eau, roche, sol" ,"categorie" : "lézard", "taille" : 0.6, "poids" : 8.5},
    {"id" : 6, "name" : "Carapuce", "type" : "eau", "faiblesses" : "plante, électrique" ,"categorie" : "minitortue", "taille" : 0.5, "poids" : 9.0},
    {"id" : 25, "name" : "Pikachu", "type" : "électrique", "faiblesses" : "sol" ,"categorie" : "souris", "taille" : 0.4, "poids" : 6.0},
]


# GET - Récupération de tous les pokémons
@app.route('/pokemons', methods=['GET'])
def get_all():
    return jsonify(pokemon_db)

# GET - Récupération d'un seul pokémon
@app.route('/pokemons/<int:pokemon_id>', methods=['GET'])
def get_one(pokemon_id):
    pokemon = next((p for p in pokemon_db if p["id"] == pokemon_id), None)
    if not pokemon:
        abort(404)
    return jsonify(pokemon)

# POST - Ajouter un nouveau pokémon
@app.route('/pokemons', methods=['POST'])
def create():
    data = request.get_json()

    new_pokemon = {
        "id" : data.get("id"),
        "name" : data.get("name"),
        "type" : data.get("type"),
        "faiblesses" : data.get("faiblesses"),
        "categorie" : data.get("categorie"),
        "taille" : data.get("taille"),
        "poids" : data.get("poids")
    }

    pokemon_db.append(new_pokemon)
    return jsonify(new_pokemon), 201

# PUT - Modifier un pokémon
@app.route('/pokemons/<int:pokemon_id>', methods=['PUT'])
def update(pokemon_id):
    data = request.get_json()
    pokemon = next((p for p in pokemon_db if p["id"] == pokemon_id), None)

    if not pokemon:
        abort(404)
    
    pokemon["name"] = data.get("name", pokemon["name"])
    pokemon["type"] = data.get("type", pokemon["type"])
    pokemon["faiblesses"] = data.get("faiblesses", pokemon["faiblesses"])
    pokemon["categorie"] = data.get("categorie", pokemon["categorie"])
    pokemon["taille"] = data.get("taille", pokemon["taille"])
    pokemon["poids"] = data.get("poids", pokemon["poids"])

    return jsonify(pokemon)

# DELETE - Supprimer un pokémon
@app.route('/pokemons/<int:pokemon_id>', methods=['DELETE'])
def delete(pokemon_id):
    global pokemon_db
    pokemon_db = [p for p in pokemon_db if p["id"] != pokemon_id]
    return jsonify({"message" : "Deleted"})

if __name__ == '__main__':
    app.run(debug=True)