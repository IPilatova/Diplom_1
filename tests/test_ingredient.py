import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from test_data import INGREDIENT_DATA


class TestIngredient:
    def test_get_valid_price(self):
        """
        Проверяет, что метод get_price возвращает правильную цену ингредиента
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_DATA['name_sauce'], INGREDIENT_DATA['price_sauce'])
        assert ingredient.get_price() == INGREDIENT_DATA['price_sauce']

    def test_get_valid_name(self):
        """
        Проверяет, что метод get_name возвращает правильное название ингредиента
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_DATA['name_sauce'], INGREDIENT_DATA['price_sauce'])
        assert ingredient.get_name() == INGREDIENT_DATA['name_sauce']

    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_ingredient_type',
        [
            (INGREDIENT_TYPE_SAUCE, INGREDIENT_DATA['name_sauce'], INGREDIENT_DATA['price_sauce'], 'SAUCE'),
            (INGREDIENT_TYPE_FILLING, INGREDIENT_DATA['name_filling'], INGREDIENT_DATA['price_filling'], 'FILLING')
        ]
    )
    def test_get_valid_type(self, ingredient_type, name, price, expected_ingredient_type):
        """
        Проверяет, что метод get_type возвращает правильный тип ингредиента
        для разных видов (соус, начинка).
        """
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_ingredient_type
