from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import InputDataForOrder as ID

from pages.base_page import BasePage
import allure


class OrderPageLocators:
    # Локаторы первой видимой части страницы
    ORDER_INPUT_NAME = (By.XPATH, './/*[@placeholder="* Имя"]')
    ORDER_INPUT_SECOND_NAME = (By.XPATH, './/*[@placeholder="* Фамилия"]')
    ORDER_INPUT_ADDRESSES = (
        By.XPATH,
        './/*[@placeholder="* Адрес: куда привезти заказ"]',
    )
    ORDER_INPUT_METRO_STATION = (By.XPATH, './/*[@placeholder="* Станция метро"]')
    ORDER_INPUT_PHONE_NUMBER = (By.XPATH, './/*[@placeholder="* Телефон: на него позвонит курьер"]')
    ORDER_BUTTON_NEXT = (By.XPATH, './/button[text()="Далее"]')
    # Локаторы второй видимой части страницы
    ORDER_INPUT_DATE = (By.XPATH, './/*[@placeholder="* Когда привезти самокат"]')
    ORDER_CALENDAR_LAST_DAY = (
        By.XPATH,
        './/div[@class="react-datepicker__week"]/following-sibling::div[last()]//*/following-sibling::div[last()]',
    )
    ORDER_DROPDOWN_RENTAL_PERIOD = (By.XPATH, '//*[@class="Dropdown-placeholder"]')
    ORDER_SELECTED_DROPDOWN_RENTAL_PERIOD = (By.XPATH, '//*[@class="Dropdown-placeholder is-selected"]')
    ORDER_INPUT_CHECKBOX_BLACK = (By.ID, 'black')
    ORDER_INPUT_CHECKBOX_GREY = (By.ID, 'grey')
    ORDER_INPUT_COMMENT = (By.XPATH, './/*[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON_BACK = (By.XPATH, './/*[text()="Назад"]')
    ORDER_BUTTON_ORDERED = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]')
    ORDR_PAGE_STATUS_CHECKBOX = (By.XPATH, '//*[contains(@class,"Order_Checkboxes__")]')
    # Локатор динамического окна
    ORDER_ACCEPT_WINDOW_TEXT = (By.XPATH, './/div[text()="Хотите оформить заказ?"]')
    ORDER_BUTTON_YES = (By.XPATH, '//button[text()="Да"]')
    ORDER_FINAL_TEXT = (By.XPATH, '//*[text()="Заказ оформлен"]')


class OrderPage(BasePage):
    timeout = 10
    @allure.step('Ввод значения в поле ввода Имя')
    def add_value_name_input(self, value=ID.FIRST_NAMES[2]):
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_INPUT_NAME)
        ).send_keys(value)

    @allure.step('Ввод значения в поле ввода Фамилии')
    def add_value_soname_input(self, value=ID.SECOND_NAMES[2]):
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_INPUT_SECOND_NAME)
        ).send_keys(value)

    @allure.step('Ввод значения в поле ввода Адрес')
    def add_value_address_input(self, value=ID.ADDRESSES[1]):
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_INPUT_ADDRESSES)
        ).send_keys(value)

    def order_selected_choice(self, element):
        return (By.XPATH, f"//*[@class='select-search__select']//*[text()='{element}']")

    @allure.step('Ввод символов и выбор из списка нужной станции')
    def choice_select_metro(self, value=ID.METRO_STATION[2], chose_value=ID.TEXT_FOR_METRO_STATION[2]):
        WebDriverWait(self.driver, OrderPage.timeout).until(EC.visibility_of_element_located(
            OrderPageLocators.ORDER_INPUT_METRO_STATION)).send_keys(value)
        station_locator = self.order_selected_choice(chose_value)
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.visibility_of_element_located(station_locator)).click()

    @allure.step('Ввод значения в поле ввода Телефона')
    def add_value_phone_input(self, value=ID.PHONE_NUMBERS[2]):
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_INPUT_PHONE_NUMBER)
        ).send_keys(value)

    @allure.step('Нажатие кнопки "Далее"')
    def click_button_next(self):
        return WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_BUTTON_NEXT)).click()

    @allure.step('Проверка на Граничные значения')
    def add_all_input_first_part_of_order_page(self, attribute_method: str = None, value=None):
        self.click_cookie_button()
        if attribute_method == 'name':
            self.add_value_name_input(value)
            self.add_value_soname_input()
            self.add_value_address_input()
            self.choice_select_metro()
            self.add_value_phone_input()
        elif attribute_method == 'soname':
            self.add_value_name_input()
            self.add_value_soname_input(value)
            self.add_value_address_input()
            self.choice_select_metro()
            self.add_value_phone_input()
        elif attribute_method == 'address':
            self.add_value_name_input()
            self.add_value_soname_input()
            self.add_value_address_input(value)
            self.choice_select_metro()
            self.add_value_phone_input()
        elif attribute_method == 'metro':
            self.add_value_name_input()
            self.add_value_soname_input()
            self.add_value_address_input()
            self.choice_select_metro(value[0], value[1])
            self.add_value_phone_input()
        elif attribute_method == 'phone':
            self.add_value_name_input()
            self.add_value_soname_input()
            self.add_value_address_input()
            self.choice_select_metro()
            self.add_value_phone_input(value)
        else:
            self.add_value_name_input()
            self.add_value_soname_input()
            self.add_value_address_input()
            self.choice_select_metro()
            self.add_value_phone_input()
        self.click_button_next()
        return self

    @allure.step('Выбор даты доставки из календаря')
    def select_date_delivery(self):
        WebDriverWait(self.driver, OrderPage.timeout).until(EC.visibility_of_element_located(
            OrderPageLocators.ORDER_INPUT_DATE)).click()
        selected_day_delivery = self.get_last_day_text()
        return selected_day_delivery, WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_CALENDAR_LAST_DAY)).click()

    def rental_selected_choice(self, element):
        return (By.XPATH, f'//*[text()="{element}"]')

    @allure.step('Выбор периода аренды')
    def choice_rental_period(self, element='сутки'):
        WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_DROPDOWN_RENTAL_PERIOD)).click()
        locator = self.rental_selected_choice(element)
        return WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            locator)).click()

    @allure.step('Выбор цвета самоката')
    def choice_scooters_color_checkbox(self, black_checkbox=False, grey_checkbox=False):
        if black_checkbox == True:
            WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
                OrderPageLocators.ORDER_INPUT_CHECKBOX_BLACK)).click()
        elif grey_checkbox == True:
            WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
                OrderPageLocators.ORDER_INPUT_CHECKBOX_GREY)).click()
        return self

    @allure.step('Ввод комментария для курьера в поле ввода')
    def add_comment_for_courier(self, text=None):
        if text != None:
            return WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
                OrderPageLocators.ORDER_INPUT_COMMENT)).send_keys(text)

    def get_last_day_text(self):
        WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_INPUT_DATE)).click()
        return WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_CALENDAR_LAST_DAY)).text

    @allure.step('Получение текста от элемента с локатором')
    def get_inputed_text(self, locator):
        return WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            locator)).text

    @allure.step('Нажатие кнопки назад')
    def click_button_back(self):
        return WebDriverWait(self.driver, OrderPage.timeout).until(EC.visibility_of_element_located(
                OrderPageLocators.ORDER_BUTTON_BACK)).click()

    @allure.step('Нажатие кнопки Заказать')
    def click_button_ordered(self):
        return WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_BUTTON_ORDERED)).click()

    @allure.step('Получение текста из сообщения о завершении заказа')
    def wait_accent_window_text(self):
        return WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_ACCEPT_WINDOW_TEXT))

    @allure.step('Получение значения элемента')
    def get_input_value(self, locator):
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.element_to_be_clickable(locator)).get_attribute('value')

    @allure.step('Получение состояния чекбоксов')
    def get_checkbox_value(self):
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDR_PAGE_STATUS_CHECKBOX)
        ).get_attribute('class')

    @allure.step('Нажатие кнопки подтверждения заказа')
    def click_confirmation_button(self):
        self.wait_accent_window_text()
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_YES)
        ).click()

    @allure.step('Получение текста успеха в создании заказа')
    def get_confirmation_window(self):
        return WebDriverWait(self.driver, OrderPage.timeout).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_FINAL_TEXT)
        ).text

    @allure.step('Ввод всех значений второй страница создания заказа')
    def add_all_input_second_part_of_order_page(self, attribute_method=None, value=None):
        self.select_date_delivery()
        if attribute_method == 'rental':
            self.choice_rental_period(value)
            self.choice_scooters_color_checkbox()
            self.add_comment_for_courier()
        elif attribute_method == 'color':
            self.choice_rental_period()
            self.choice_scooters_color_checkbox(value[0], value[1])
            self.add_comment_for_courier()
        elif attribute_method == 'comment':
            self.choice_rental_period()
            self.choice_scooters_color_checkbox()
            self.add_comment_for_courier(value)
        else:
            self.choice_rental_period()
            self.choice_scooters_color_checkbox()
            self.add_comment_for_courier()
        return self
