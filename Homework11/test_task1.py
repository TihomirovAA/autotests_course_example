# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_sbis():
    driver = webdriver.Chrome()
    sbis_site = 'https://sbis.ru/'
    sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
    contacts = 'Контакты'
    try:
        print(f'Переходим на сайт {sbis_site}')
        driver.get(sbis_site)
        sleep(3)
        print('Проверить адрес сайта и заголовок страницы')
        assert driver.current_url == sbis_site, 'Неверный адрес сайта'
        assert driver.title == sbis_title, 'Неверный заголовок сайта'

        print(f'Переходим в раздел {contacts}')
        contacts_btn = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
        assert contacts_btn.is_displayed()
        contacts_btn.click()

        print('ищем банер "Тензор" и кликаем на него')
        sleep(3)
        tensor_banner = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
        assert tensor_banner.is_displayed()
        tensor_banner.click()

        print('проверяем что на странице есть блок новости "Сила в людях"')
        driver.switch_to.window(driver.window_handles[1])
        sleep(3)
        man_power_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
        assert man_power_block.is_displayed()

        print('клик в "Подробнее", проверка что открывается https://tensor.ru/about')
        about_button = driver.find_element(By.CSS_SELECTOR, '[href="/about"]')
        assert about_button.is_displayed()
        about_button.click()
        sleep(3)
        assert driver.current_url == 'https://tensor.ru/about', 'Неверно открыт сайт'


    finally:
        driver.quit()