import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_list(self, db):
        """
        Проверяет, что метод available_buns возвращает список
        """
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_count_available_buns(self, db):
        """
        Проверяет, что доступных булочек в базе - 3 наименования
        """
        buns = db.available_buns()
        assert len(buns) == 3

    @pytest.mark.parametrize(
        'name, expected_price',
        [
            ('black bun', 100),
            ('white bun', 200),
            ('red bun', 300),
        ]
    )
    def test_bun_price_by_name(self, db, name, expected_price):
        """
        Проверяет, что цена булочки с заданным названием соответствует ожидаемой
        """
        buns = db.available_buns()
        for bun in buns:
            if bun.name == name:
                assert bun.price == expected_price

    def test_available_ingredients_returns_list(self, db):
        """
        Проверяет, что метод available_ingredients возвращает список
        """
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_count_available_ingredients(self, db):
        """
        Проверяет, что в базе доступно 6 ингредиентов.
        """
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_count_available_sauces(self, db):
        """
        Проверяет, что среди ингредиентов 3 наименования соуса
        """
        ingredients = db.available_ingredients()
        sauces = [ing for ing in ingredients if ing.type == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_count_available_fillings(self, db):
        """
        Проверяет, что среди ингредиентов ровно 3 наименования начинки
        """
        ingredients = db.available_ingredients()
        fillings = [ing for ing in ingredients if ing.type == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    @pytest.mark.parametrize(
        "name, expected_price",
        [
            ("hot sauce", 100),
            ("sour cream", 200),
            ("chili sauce", 300),
            ("cutlet", 100),
            ("dinosaur", 200),
            ("sausage", 300),
        ]
    )
    def test_ingredient_price_by_name(self, db, name, expected_price):
        """
        Проверяет, что цена ингредиента с заданным названием соответствует ожидаемой
        """
        ingredients = db.available_ingredients()
        for ing in ingredients:
            if ing.name == name:
                assert ing.price == expected_price
