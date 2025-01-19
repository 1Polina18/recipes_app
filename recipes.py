import json
import os
from utils import save_recipes

RECIPES_FILE = "recipes.json"

def load_recipes():
    if not os.path.exists(RECIPES_FILE):
        return {}
    with open(RECIPES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def add_recipe(recipes, name, ingredients):
    recipes[name] = ingredients
    save_recipes(recipes)

def list_recipes(recipes):
    if not recipes:
        print("No recipes found.")
        return
    for name, ingredients in recipes.items():
        print(f"- {name}: {', '.join(ingredients)}")

def delete_recipe(recipes, name):
    if name in recipes:
        del recipes[name]
        save_recipes(recipes)
        print(f"Recipe '{name}' removed.")
    else:
        print(f"Recipe '{name}' not found.")

def search_recipes_by_ingredient(recipes, ingredient):
    found_recipes = {name: ing for name, ing in recipes.items() if ingredient.lower() in (ing.lower() for ing in ing)}
    return found_recipes

if __name__ == "__main__":
    recipes = load_recipes()
    while True:
        print("\n1) Add Recipe")
        print("2) List Recipes")
        print("3) Remove Recipe")
        print("4) Search Recipe by Ingredient")
        print("5) Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            ingredients = [ing.strip() for ing in ingredients]
            add_recipe(recipes, name, ingredients)
        elif choice == "2":
            list_recipes(recipes)
        elif choice == "3":
            name = input("Enter recipe name to remove: ")
            delete_recipe(recipes, name)
        elif choice == "4":
            ingredient = input("Enter ingredient to search for: ")
            found_recipes = search_recipes_by_ingredient(recipes, ingredient)
            if found_recipes:
                print(f"Recipes containing '{ingredient}':")
                for name, ingredients in found_recipes.items():
                    print(f"- {name}: {', '.join(ingredients)}")
            else:
                print(f"No recipes found with ingredient '{ingredient}'.")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
