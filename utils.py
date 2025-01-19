import json
import os

RECIPES_FILE = "recipes.json"

def save_recipes(recipes):
    with open(RECIPES_FILE, "w", encoding="utf-8") as f:
        json.dump(recipes, f, ensure_ascii=False, indent=4)
