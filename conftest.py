import pytest
from selenium import webdriver
import allure

import links
from pages.order_page import OrderPage as OP
from selenium.webdriver.firefox.options import Options


@allure.step('Запуск драйвера FIrefox')
@pytest.fixture
def start_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@allure.step('Выполнение преусловия заполнения валидными данными первой страница формы регистрации заказа')
@pytest.fixture
def add_values_first_order_page(start_driver):
    driver = OP(start_driver)
    driver.go_to_site(links.ORDER_PAGE_URL)
    driver.add_all_input_first_part_of_order_page()
    return driver
