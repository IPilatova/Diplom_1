import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from test_data import INGREDIENT_DATA
from test_data import BUN_DATA


class TestBurger:

    def test_init_default_value_bun(self, burger):
        """
        Проверяет, что при инициализации объекта Burger атрибут bun по умолчанию равен None.
        """
        assert burger.bun is None

    def test_init_default_value_ingredients(self, burger):
        """
        Проверяет, что при инициализации объекта Burger список ингредиентов пуст.
        """
        assert burger.ingredients == []

    def test_set_buns(self, burger):
        """
        Проверяет корректную установку данных булочки в бургер методом set_buns
        """
        bun = Bun(BUN_DATA['name'], BUN_DATA['price'])
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger):
        """
        Проверяет добавление ингредиента в бургер
        """
        mock_ingredient = Mock()
        mock_ingredient.get_ingredient_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = INGREDIENT_DATA['name_sauce']
        mock_ingredient.get_price.return_value = INGREDIENT_DATA['price_sauce']
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger):
        """
        Проверяет удаление ингредиента по индексу из списка ингредиентов бургера
        """
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_2

    def test_move_ingredient(self, burger):
        """
        Проверяет перемещение ингредиента с одного индекса на другой внутри списка ингредиентов
        """
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    @pytest.mark.parametrize(
        'bun_id, ingredient_ids, expected_price',
        [
            (1, [1, 3], 700),
            (0, [], 200),
            (2, [0, 4], 900),
            (2, [5], 900),
            (0, [2, 3, 3], 700)
        ]
    )
    def test_get_price(self, db, burger, bun_id, ingredient_ids, expected_price):
        """
        Проверяет вычисление итоговой стоимости бургера в зависимости от выбранной булочки и ингредиентов

        Args:
        bun_id (int): индекс булочки из базы данных
        ingredient_ids (list[int]): индексы ингредиентов из базы данных
        expected_price (int): ожидаемая итоговая цена
        """
        burger.set_buns(db.available_buns()[bun_id])
        for i in ingredient_ids:
            burger.add_ingredient(db.available_ingredients()[i])
        assert burger.get_price() == expected_price


    def test_get_receipt(self, db, burger):
        """
        Проверяет корректное формирование текста чека бургера
        """
        burger.set_buns(db.available_buns()[1])
        burger.add_ingredient(db.available_ingredients()[1])
        burger.add_ingredient(db.available_ingredients()[3])
        expected_receipt = "(==== white bun ====)\n" \
                           "= sauce sour cream =\n" \
                           "= filling cutlet =\n" \
                           "(==== white bun ====)\n\n" \
                           "Price: 700"
        assert expected_receipt == burger.get_receipt()






