fruit = input("Item: ").lower()

calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100,
}

if fruit in calories:
    print(f"Calories: {calories[fruit]}")
