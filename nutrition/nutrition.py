# dicionário com as frutas e suas calorias
frutas = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew": 50,
    "kiwifruit": 90,
    "lemon": 20,
    "lime": 20,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberry": 50,
    "sweet cherries":100,
    "tangerine":50,
    "watermelon": 80
}

# solicita ao usuário que insira uma fruta
fruta = input("Insira uma fruta: ")

# verifica se a fruta está no dicionário e exibe as calorias em caso afirmativo
if fruta.lower() in frutas:
    print(f"A porção de {fruta} tem {frutas[fruta.lower()]} calorias.")
else:
    print("")
