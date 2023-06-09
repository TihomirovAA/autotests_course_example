# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста



from selenium.webdriver import Keys, ActionChains

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_sbis():
    driver = webdriver.Chrome()
    site = 'https://fix-online.sbis.ru/'
    try:
        print('Перейти на страницу авторизации')
        driver.get(site)
        sleep(1)

        print('Авторизоваться')
        user_login, user_password = 'бетмен', 'Бетмен123'
        login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
        login.send_keys(user_login, Keys.ENTER)
        sleep(1)
        password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
        password.send_keys(user_password, Keys.ENTER)
        sleep(3)
        driver.refresh()
        sleep(3)

        print(f'Переходим в раздел Контакты')
        contacts_btn = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
        contacts_btn.click()
        sleep(1)
        contacts_sub_menu_btn = driver.find_element(By.CSS_SELECTOR, '[href="/page/dialogs"]')
        contacts_sub_menu_btn.click()
        sleep(3)

        print('Отправляем самому себе сообщение')
        add_btn = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
        add_btn.click()
        sleep(3)
        search_input = driver.switch_to.active_element
        search_input.send_keys('Белоярова')
        sleep(2)
        search_input.send_keys(Keys.ENTER)
        sleep(2)
        dialog_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
        message = 'привет'
        dialog_input.send_keys(message + Keys.CONTROL + Keys.ENTER)


        print(f'Проверяем что сообдещние с текстом {message} отображается в реестре')
        sleep(2)
        last_messages = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
        assert last_messages.text == message, 'сообщение не отображается в реестре'

        print('Удаляем сообщение')
        action_chains = ActionChains(driver)
        action_chains.move_to_element(last_messages)
        action_chains.context_click(last_messages)
        action_chains.perform()
        sleep(1)
        delete_btn = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
        delete_btn.click()
        last_messages = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
        sleep(1)
        assert last_messages.text != message, 'сообщение не удалено'

    finally:
        driver.quit()