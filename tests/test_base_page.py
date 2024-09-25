import links
from pages.base_page import BasePage
from pages.base_page import BasePageLocators
from pages.main_page import MainPageLocators
from pages.order_page import OrderPageLocators
import allure


class TestBasePage:
    @allure.title("Проверка клика по слову Яндекс в Хедере")
    def test_click_yandex_logo_true(self, start_driver):
        base_page = BasePage(start_driver)
        base_page.go_to_site(links.MAIN_PAGE_URL)
        base_page.click_element(BasePageLocators.BASE_HEADER_YANDEX_LINK)
        base_page.switch_to_window()
        base_page.find_element(BasePageLocators.MAIN_DZEN_MAIN_TEXT)
        assert base_page.get_url() == links.DZEN_URL

    @allure.title("Проверка клика по слову Самокат в хедере")
    def test_click_scooter_logo_true(self, start_driver):
        base_page = BasePage(start_driver)
        base_page.go_to_site(links.MAIN_PAGE_URL)
        base_page.click_element(BasePageLocators.BASE_HEADER_SCOOTER_LINK)
        base_page.find_element(MainPageLocators.MAIN_TITLE_SCOOTER_AT_DAYS)
        assert base_page.get_url() == links.MAIN_PAGE_URL

    @allure.title("Клик по кнопке Заказать в хедере")
    def test_click_order_button_true(self, start_driver):
        base_page = BasePage(start_driver)
        base_page.go_to_site(links.MAIN_PAGE_URL)
        base_page.click_element(BasePageLocators.BASE_HEADER_ORDER_BUTTON)
        base_page.find_element(OrderPageLocators.ORDER_INPUT_NAME)
        assert base_page.get_url() == links.ORDER_PAGE_URL
