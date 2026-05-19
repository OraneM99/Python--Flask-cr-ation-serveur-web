# CRUD API avec Flask

Ce projet est une API REST simple réalisée avec **Flask** en Python. Elle permet de gérer une liste de Pokémon avec les opérations CRUD.

- CREATE (Créer)
- Reade (Lire)
- Update (Mettre à jour)
- DELETE (Supprimer)

## Installation

### 1. Cloner le projet

```git
git clone https://github.com/OraneM99/Python--Flask-cr-ation-serveur-web
cd flask-demo
```

### 2. Créer un environnement virtuel

```git
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances

```git
pip install flask
```

### 4. Lancer l'application

```git
python app.py
```

Par défaut l'API est accessbile sur [http://127.0.0.1:5050](http://127.0.0.1:5050)

## Endpoints API

### 1. GET - Récupération de tous les pokémons

`GET /pokemons`

#### Réponse

```json
[
    {
        "id" : 1,
        "name" : "Bulbizarre",
        "type" : "plante, poison",
        "faiblesses" : "feu, vol, glace, psy",
        "categorie" : "graine",
        "taille" : 0.7,
        "poids" : 6.9
    }
]
```

### 2. GET - Récupération d'un seul pokémon

`GET /pokemons/<id>`

#### Exemple

`GET /pokemons/1`

### 3. POST - Ajouter un nouveau pokémon

`POST /pokemons`

#### Body (JSON)

```json
{
    "name" : "Dracaufeu",
    "type" : "feu, vol",
    "faiblesses" : "eau, électrique, roche",
    "categorie" : "flamme",
    "taille" : 1.7,
    "poids" : 90.5
}
```

#### Réponse

```json
{
    "id" : "2",
    "name" : "Dracaufeu",
    "type" : "feu, vol",
    "faiblesses" : "eau, électrique, roche",
    "categorie" : "flamme",
    "taille" : 1.7,
    "poids" : 90.5
}
```

### 4. PUT - Modifier un pokémon

`PUT /pokemons/<id>`

#### Exemple

```json
{
    "type" : "feu"
}

```

### 5. DELETE - Supprimer un pokémon

`DELETE /pokemons/<id>`

#### Réponse

```json
{
    "message" : "Deleted"
}
```

## Remarques
Les données sont stockées en mémoire, elle disparaissent au démarrage, ce projet est destiné à l'apprentissage.