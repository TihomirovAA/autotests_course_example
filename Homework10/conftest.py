import datetime
import pytest


@pytest.fixture(scope='class')
def time_class():
    print(f"\nвремя начала выполнение класса {datetime.datetime.now().strftime('%H:%M:%S:%f')}")
    yield
    print(f"\nвремя окончания выполнение класса {datetime.datetime.now().strftime('%H:%M:%S:%f')}")


@pytest.fixture()
def time_tests():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'\nВремя выполнения теста {end - start}')

