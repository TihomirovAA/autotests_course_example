# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('time_class')
class TestMy:

    @pytest.mark.parametrize('dividend, divider, result', [
        pytest.param(2, 1, 2, marks=pytest.mark.smoke),
        pytest.param(3, -3, -1),
        pytest.param(0, 3, 0)])
    def test_positive(self, dividend, divider, result, time_tests):
        assert all_division(dividend, divider) == result

    @pytest.mark.parametrize('dividend, divider, result', [
        pytest.param(2, 0, ZeroDivisionError, marks=pytest.mark.skip("bad test")),
        pytest.param(2, '1', TypeError)])
    def test_negative(self, dividend, divider, result):
        with pytest.raises(result):
            all_division(dividend, divider)
