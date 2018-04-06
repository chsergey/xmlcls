# -*- coding: utf-8 -*-
"""
Examples of usage custom classes
"""

from xmlcls import XMLFile
from xmlcls.xml_errors import (
    XMLSyntaxError,
    DocumentInvalid
)

# import custom wrapper classes
import recipes

with open('./recipes/recipes.xml', 'rb') as f:
    xml_text = f.read()

with open('./recipes/recipes.xsd', 'rb') as f:
    xsd_text = f.read()

xml = XMLFile(xml_text)

# validating xml
is_valid = xml.is_valid(xsd_str=xsd_text)  # returns bool

try:
    xml.assert_valid(xsd_text)
except (XMLSyntaxError, DocumentInvalid) as e:
    # get errors from Exception
    str(e)
    # or get errors from log
    errors = xml.error_log


# get root element
collection = recipes.Collection(xml)

# get list of recipes
# <class 'list'>: [recipe, recipe, recipe, recipe, recipe]
recipes_list = recipes.RecipesList(collection)


# get recipes titles as
# [
#   'Beef Parmesan with Garlic Angel Hair Pasta',
#   'Ricotta Pie', 'Linguine Pescadoro',
#   'Zuppa Inglese',
#   'Cailles en Sarcophages'
# ]
recipes_titles_list = [recipe.title for recipe in recipes_list]  # type: list


# get first recipe object
first_recipe = recipes_list[0]  # type: recipes.Recipe


# nutrition: {'calories': '1167', 'carbohydrates': '45', 'protein': '32', 'fat': '23'}
first_recipe_nutrition = first_recipe.nutrition


#   Make the meat ahead of time, and refrigerate over night, the acid in the
#   tomato sauce will tenderize the meat even more. If you do this, save the
#   mozzarella till the last minute.
first_recipe_comment = first_recipe.comment


# <class 'list'>: [
#   ingredient: {'name': 'beef cube steak', 'amount': '1.5', 'unit': 'pound'},
#   ingredient: {'name': 'onion, sliced into thin rings', 'amount': '1'},
#   ingredient: {'name': 'green bell pepper, sliced in rings', 'amount': '1'},
#   ...
# ]
ingredients = first_recipe.ingredients  # type: list


# "1.5 pound of beef cube steak"
first_ingredient_text = ' '.join([
    ingredients[0].amount,   # get attribute by dot notation
    ingredients[0].unit,
    'of',
    ingredients[0]['name'],  # or by dict notation
])


# <class 'list'>: [
#   'Preheat oven to 350 degrees F (175 degrees C).',
#   'Cut cube steak into serving size pieces. Coat meat with the bread crumbs...',
#   'Bake at 350 degrees F (175 degrees C) for 30 to 45 minutes, depending on...',
#   'Boil pasta al dente. Drain, and toss in butter and 1 teaspoon garlic...'
# ]
steps = first_recipe.steps  # type: list


# get second recipe from list with complex ingredient
second_recipe = recipes_list[1]  # type: recipes.Recipe


# get first ingredient. it is complex
ingredient = second_recipe.ingredients[0]  # type: recipes.Ingredient


# get ingredients of ingredient
# <class 'list'>: [
#   ingredient: {'amount': '3', 'name': 'ricotta cheese', 'unit': 'pound'},
#   ingredient: {'amount': '12', 'name': 'eggs'},
#   ingredient: {'amount': '2', 'name': 'white sugar', 'unit': 'cup'},
#   ingredient: {'amount': '2', 'name': 'vanilla extract', 'unit': 'teaspoon'},
#   ingredient: {'amount': '0.25', 'name': 'semisweet chocolate chips', 'unit': 'cup'}
# ]
ingredient_ingredients = ingredient.ingredients
