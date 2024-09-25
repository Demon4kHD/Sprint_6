import allure
import links
from data import AnswersTextMainPage as AT
from pages.main_page import MainPage
from pages.main_page import MainPageLocators as MPL
from pages.order_page import OrderPageLocators as OPL


class TestMainPage:
    @allure.title("Сравнение текста ответа на первый вопрос с эталлонным")
    def test_first_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.scroll_to_answer(MPL.MAIN_FOURTH_QUESTION)
        main_page.click_element(MPL.MAIN_FIRST_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_FIRST_ANSWER)
        assert answer_text == AT.MAIN_TEXT_FIRST_ANSWER

    @allure.title("Сравнение текста ответа на второй вопрос с эталлонным")
    def test_second_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.scroll_to_answer(MPL.MAIN_SECOND_QUESTION)
        main_page.click_element(MPL.MAIN_SECOND_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_SECOND_ANSWER)
        assert answer_text == AT.MAIN_TEXT_SECOND_ANSWER

    @allure.title("Сравнение текста ответа на третий вопрос с эталлонным")
    def test_third_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.scroll_to_answer(MPL.MAIN_THIRD_QUESTION)
        main_page.click_element(MPL.MAIN_THIRD_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_THIRD_ANSWER)
        assert answer_text == AT.MAIN_TEXT_THIRD_ANSWER

    @allure.title("Сравнение текста ответа на четвертый вопрос с эталлонным")
    def test_fourth_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_TITLE_SCOOTER_AT_DAYS)
        main_page.scroll_to_answer(MPL.MAIN_FOURTH_QUESTION)
        main_page.click_element(MPL.MAIN_FOURTH_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_FOURTH_ANSWER)
        assert answer_text == AT.MAIN_TEXT_FOURTH_ANSWER

    @allure.title("Сравнение текста ответа на пятый вопрос с эталлонным")
    def test_fifth_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.scroll_to_answer(MPL.MAIN_FIFTH_QUESTION)
        main_page.click_element(MPL.MAIN_FIFTH_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_FIFTH_ANSWER)
        assert answer_text == AT.MAIN_TEXT_FIFTH_ANSWER

    @allure.title("TСравнение текста ответа на шестой вопрос с эталлонным")
    def test_sixth_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.scroll_to_answer(MPL.MAIN_SIXTH_QUESTION)
        main_page.click_element(MPL.MAIN_SIXTH_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_SIXTH_ANSWER)
        assert answer_text == AT.MAIN_TEXT_SIXTH_ANSWER

    @allure.title("Сравнение текста ответа на седьмой вопрос с эталлонным")
    def test_seventh_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.scroll_to_answer(MPL.MAIN_SEVENTH_QUESTION)
        main_page.click_element(MPL.MAIN_SEVENTH_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_SEVENTH_ANSWER)
        assert answer_text == AT.MAIN_TEXT_SEVENTH_ANSWER

    @allure.title("Сравнение текста ответа на восьмой вопрос с эталлонным")
    def test_eighth_answer(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.find_element(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.scroll_to_answer(MPL.MAIN_EIGHTH_QUESTION)
        main_page.click_element(MPL.MAIN_EIGHTH_QUESTION)
        answer_text = main_page.get_answer_text(MPL.MAIN_EIGHTH_ANSWER)
        assert answer_text == AT.MAIN_TEXT_EIGHTH_ANSWER

    @allure.title("Клик на кнопку Заказать в теле главной страницы")
    def test_main_button_order(self, start_driver):
        main_page = MainPage(start_driver)
        main_page.go_to_site(links.MAIN_PAGE_URL)
        main_page.scroll_to_answer(MPL.MAIN_BODY_ORDER_BUTTON)
        main_page.click_element(MPL.MAIN_BODY_ORDER_BUTTON)
        assert main_page.find_element(OPL.ORDER_INPUT_NAME)
