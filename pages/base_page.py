from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePageLocators:
    BASE_HEADER_YANDEX_LINK = (By.XPATH, './/*[@href="//yandex.ru"]')
    BASE_HEADER_SCOOTER_LINK = (By.XPATH, './/*[@alt="Scooter"]')
    BASE_HEADER_ORDER_BUTTON = (By.XPATH, './/*[contains(@class,"Header_Header")]//*[text()="Заказать"]',)
    MAIN_DZEN_MAIN_TEXT = (By.XPATH, './/*[text()="Главное"]')
    BASE_PAGE_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')


class BasePage:
    timeout = 10
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Преход на сайт')
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Клик на элемент')
    def click_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Получение URL драйвера')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Переключение на другую вкладку')
    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Закрытия уведомления об использовании cookie')
    def click_cookie_button(self):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(
            BasePageLocators.BASE_PAGE_COOKIE_BUTTON)).click()
