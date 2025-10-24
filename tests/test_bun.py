from praktikum.bun import Bun
from test_data import BUN_DATA


class TestBun:
    def test_get_valid_name(self):
        """
        Проверяет, что метод get_name возвращает правильное название булочки
        """
        bun = Bun(BUN_DATA['name'], BUN_DATA['price'])
        assert bun.get_name() == BUN_DATA['name']

    def test_get_valid_price(self):
        """
        Проверяет, что метод get_price возвращает правильную цену булочки
        """
        bun = Bun(BUN_DATA['name'], BUN_DATA['price'])
        assert bun.get_price() == BUN_DATA['price']
