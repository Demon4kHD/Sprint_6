from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
import allure


class MainPageLocators:
    MAIN_TITLE_SCOOTER_AT_DAYS = (By.XPATH, './/*[contains(@class ,"Home_Header")]')
    # Локаторы вопросов
    MAIN_FIRST_QUESTION = (By.ID, 'accordion__heading-0')
    MAIN_SECOND_QUESTION = (By.ID, 'accordion__heading-1')
    MAIN_THIRD_QUESTION = (By.ID, 'accordion__heading-2')
    MAIN_FOURTH_QUESTION = (By.ID, 'accordion__heading-3')
    MAIN_FIFTH_QUESTION = (By.ID, 'accordion__heading-4')
    MAIN_SIXTH_QUESTION = (By.ID, 'accordion__heading-5')
    MAIN_SEVENTH_QUESTION = (By.ID, 'accordion__heading-6')
    MAIN_EIGHTH_QUESTION = (By.ID, 'accordion__heading-7')
    # Локаторы ответов
    MAIN_FIRST_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-0"]')
    MAIN_SECOND_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-1"]')
    MAIN_THIRD_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-2"]')
    MAIN_FOURTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-3"]')
    MAIN_FIFTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-4"]')
    MAIN_SIXTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-5"]')
    MAIN_SEVENTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-6"]')
    MAIN_EIGHTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-7"]')
    # Кнопка перехода на страницу /order
    MAIN_BODY_ORDER_BUTTON = (By.XPATH, '//button[contains(@class,"Button_Middle")]')


class MainPage(BasePage):
    @allure.step('Получение текста элемента с локатором')
    def get_answer_text(self, answer_locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(answer_locator)
        ).text

    @allure.step('Скролл до элемента  с локатором ')
    def scroll_to_answer(self, answer_locator):
        element = self.driver.find_element(*answer_locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)
