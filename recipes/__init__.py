# -*- coding: utf-8 -*-
"""
Example classes for recipes.xml elements
"""

from xmlcls import XMLElement


class Collection(XMLElement):
    """
    Class for root element "collection"
    """
    xpath = None


class Description(XMLElement):
    """
    Class for element "description"
    """
    xpath = './description'


class Title(XMLElement):
    """
    Class for element "title"
    """
    xpath = './title'


class Comment(XMLElement):
    """
    Class for element "comment"
    """
    xpath = './comment'


class PreparationStep(XMLElement):
    """
    Class for element "step"
    """
    xpath = './step'


class PreparationStepsList(XMLElement):
    """
    Class for element "preparation"
    """
    xpath = './preparation/step'
    _list_item_class = PreparationStep


class Ingredient(XMLElement):
    """
    Class for element "ingredient"
    This element can contain another "ingredient"
    """
    xpath = './ingredient'

    @property
    def ingredients(self):
        return IngredientsList(self)


class Nutrition(XMLElement):
    """
    Class for element "nutrition"
    """
    xpath = './nutrition'


class Recipe(XMLElement):
    """
    Class for element "recipe"
    """
    xpath = './recipe'

    @property
    @XMLElement.as_text
    def title(self):
        return Title(self)

    @property
    @XMLElement.as_text
    def comment(self):
        return Comment(self)

    @property
    @XMLElement.as_text
    def steps(self):
        return PreparationStepsList(self)

    @property
    def ingredients(self):
        return IngredientsList(self)

    @property
    def nutrition(self):
        return Nutrition(self)


class RecipesList(XMLElement):
    """
    Class for list of "recipe" elements
    """
    xpath = './recipe'

    _list_item_class = Recipe


class IngredientsList(XMLElement):
    """
    Class for list of "ingredient" elements
    """
    xpath = './ingredient'
    _list_item_class = Ingredient
