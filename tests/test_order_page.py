import allure
import pytest

import helper
from data import InputDataForOrder as ID
from links import ORDER_PAGE_URL
from pages.order_page import OrderPage
from pages.order_page import OrderPageLocators as OPL


class TestOrderPage:
    '''Проверка первой части страницы заказа'''

    @allure.title('Тест сохранения введенных данных после перехода на следующую страницу и возврату')
    def test_first_page_is_safe_input_values_after_click_button_back(self, start_driver):
        first_order_page = OrderPage(start_driver)
        first_order_page.go_to_site(ORDER_PAGE_URL)
        first_order_page.add_all_input_first_part_of_order_page()
        first_order_page.click_button_back()
        assert first_order_page.get_input_value(OPL.ORDER_INPUT_NAME) == ID.FIRST_NAMES[2]
        assert first_order_page.get_input_value(OPL.ORDER_INPUT_SECOND_NAME) == ID.SECOND_NAMES[2]
        assert ID.ADDRESSES[1] in first_order_page.get_input_value(OPL.ORDER_INPUT_ADDRESSES)
        assert first_order_page.get_input_value(OPL.ORDER_INPUT_METRO_STATION) == ID.TEXT_FOR_METRO_STATION[2]
        assert first_order_page.get_input_value(OPL.ORDER_INPUT_PHONE_NUMBER) == ID.PHONE_NUMBERS[2]

    @allure.title('Тест на граничные значения поля ввода Имени')
    @pytest.mark.parametrize('param', ID.FIRST_NAMES)
    def test_add_valid_first_name_in_input(self, start_driver, param):
        first_order_page = OrderPage(start_driver)
        first_order_page.go_to_site(ORDER_PAGE_URL)
        first_order_page.add_all_input_first_part_of_order_page('name', param)
        assert first_order_page.find_element(OPL.ORDER_BUTTON_ORDERED)

    @allure.title('Тест на граничные значения полей ввода')
    @pytest.mark.parametrize('param', ID.SECOND_NAMES)
    def test_add_valid_second_name_in_input(self, start_driver, param):
        first_order_page = OrderPage(start_driver)
        first_order_page.go_to_site(ORDER_PAGE_URL)
        first_order_page.add_all_input_first_part_of_order_page('soname', param)
        assert first_order_page.find_element(OPL.ORDER_BUTTON_ORDERED)

    @allure.title('Тест на граничные значения поля ввода Адреса')
    @pytest.mark.parametrize('param', ID.ADDRESSES)
    def test_add_valid_addresses_in_input(self, start_driver, param):
        first_order_page = OrderPage(start_driver)
        first_order_page.go_to_site(ORDER_PAGE_URL)
        first_order_page.add_all_input_first_part_of_order_page('address', param)
        assert first_order_page.find_element(OPL.ORDER_BUTTON_ORDERED)

    metro_values = helper.two_list_in_one(ID.METRO_STATION, ID.TEXT_FOR_METRO_STATION)

    @allure.title('Тест на граничные значения поля выбора станции Метро')
    @pytest.mark.parametrize('param', metro_values)
    def test_add_valid_metro_in_input(self, start_driver, param):
        first_order_page = OrderPage(start_driver)
        first_order_page.go_to_site(ORDER_PAGE_URL)
        first_order_page.add_all_input_first_part_of_order_page('metro', param)
        assert first_order_page.find_element(OPL.ORDER_BUTTON_ORDERED)

    @allure.title('Тест на граничные значения поля ввода Телефон')
    @pytest.mark.parametrize('param', ID.PHONE_NUMBERS)
    def test_add_valid_phone_number_in_input(self, start_driver, param):
        first_order_page = OrderPage(start_driver)
        first_order_page.go_to_site(ORDER_PAGE_URL)
        first_order_page.add_all_input_first_part_of_order_page('phone', param)
        assert first_order_page.find_element(OPL.ORDER_BUTTON_ORDERED)

    '''Проверка второй части страницы заказа'''

    @allure.title('Тест сохранение значений всех полей на второй страницу после перехода к первой и обратно')
    def test_second_page_is_safe_input_values_after_click_button_back(self, add_values_first_order_page):
        second_order_page = add_values_first_order_page
        selected_day_delivery = second_order_page.get_last_day_text()
        second_order_page.add_all_input_second_part_of_order_page('comment', ID.COMMENT_FOR_COURIER[3])
        second_order_page.click_button_back()
        second_order_page.click_button_next()
        assert selected_day_delivery in second_order_page.get_input_value(OPL.ORDER_INPUT_DATE)
        assert ID.RENTAL_PERIOD[0] == second_order_page.get_inputed_text(OPL.ORDER_SELECTED_DROPDOWN_RENTAL_PERIOD)
        assert ID.CHECKBOX_ACTIVE not in second_order_page.get_checkbox_value()
        assert ID.COMMENT_FOR_COURIER[3] == second_order_page.get_input_value(OPL.ORDER_INPUT_COMMENT)

    @allure.title('Тест на все возможные вариант выбора выпадающего списка')
    @pytest.mark.parametrize('value', ID.RENTAL_PERIOD)
    def test_select_dropdown_values_true(self, add_values_first_order_page, value):
        second_order_page = add_values_first_order_page
        second_order_page.add_all_input_second_part_of_order_page('rental', value)
        second_order_page.click_button_ordered()
        assert second_order_page.wait_accent_window_text()

    posible_value = helper.two_list_in_one(ID.BLACK_CHECKBOX_POSIBLE_VALUES, ID.GREY_CHECKBOX_POSIBLE_VALUES)

    @allure.title('Тест на положение обоих чекбоксов')
    @pytest.mark.parametrize('value', posible_value)
    def test_select_checkbox_values_true(self, add_values_first_order_page, value):
        second_order_page = add_values_first_order_page
        second_order_page.add_all_input_second_part_of_order_page('color', value)
        second_order_page.click_button_ordered()
        assert second_order_page.wait_accent_window_text()

    @allure.title('Тест на граничные значения поля ввода Комментария для курьера')
    @pytest.mark.parametrize('value', ID.COMMENT_FOR_COURIER)
    def test_select_comment_true(self, add_values_first_order_page, value):
        second_order_page = add_values_first_order_page
        second_order_page.add_all_input_second_part_of_order_page('comment', value)
        second_order_page.click_button_ordered()
        assert second_order_page.wait_accent_window_text()

    @allure.title('Тест на завершение заказа')
    def test_make_order_true(self, add_values_first_order_page):
        second_order_page = add_values_first_order_page
        second_order_page.add_all_input_second_part_of_order_page()
        second_order_page.click_button_ordered()
        second_order_page.click_confirmation_button()
        assert ID.FINAL_TEXT_ORDER in second_order_page.get_confirmation_window()
