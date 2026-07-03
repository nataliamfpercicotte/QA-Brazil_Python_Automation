from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code


class UrbanRoutesPage:

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    CALL_A_TAXI_BUTTON = (By.XPATH, '//button[text()="Chamar um táxi"]')
    COMFORT_CARD = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]/..')

    PHONE_NUMBER_BUTTON = (By.XPATH, '//div[text()="Número de telefone"]')
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, '//button[text()="Próximo"]')
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Confirmar"]')
    INSERTED_PHONE_NUMBER = (By.CLASS_NAME, "np-text")

    PAYMENT_METHOD_BUTTON = (
        By.XPATH,
        '//div[@class="pp-button filled"]//div[contains(text(), "Método de pagamento")]'
    )

    ADD_CARD_BUTTON_ROW = (
        By.XPATH,
        '//div[text()="Adicionar cartão"]'
    )

    CARD_NUMBER_INPUT = (
        By.CSS_SELECTOR,
        "input.card-input#number"
    )

    CARD_CODE_INPUT = (
        By.CSS_SELECTOR,
        "input.card-input#code"
    )

    ADD_CARD_BUTTON = (
        By.XPATH,
        '//button[text()="Adicionar"]'
    )

    CURRENT_PAYMENT_METHOD = (
        By.CLASS_NAME,
        "pp-value-text"
    )

    CLOSE_PAYMENT_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"payment-picker") and contains(@class,"open")]//button[contains(@class,"section-close")]'
    )

    COMMENT_INPUT = (By.ID, "comment")

    BLANKET_SWITCH = (
        By.XPATH,
        '//div[text()="Cobertor e lençóis"]/following::span[@class="slider round"][1]'
    )

    BLANKET_CHECKBOX = (
        By.XPATH,
        '//div[text()="Cobertor e lençóis"]/following::input[@type="checkbox"][1]'
    )

    ICE_CREAM_PLUS = (
        By.XPATH,
        '(//div[@class="counter-plus"])[1]'
    )

    ICE_CREAM_COUNT = (
        By.XPATH,
        '(//div[@class="counter-value"])[1]'
    )

    ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
    CAR_SEARCH_MODAL = (By.CLASS_NAME, "order")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def _click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_value(self, locator):
        return self._find(locator).get_attribute("value")

    def _get_text(self, locator):
        return self._find(locator).text

    def _press_tab(self):
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    def enter_locations(self, from_text, to_text):
        self._type(self.FROM_FIELD, from_text)
        self._type(self.TO_FIELD, to_text)

    def get_from_location(self):
        return self._get_value(self.FROM_FIELD)

    def get_to_location(self):
        return self._get_value(self.TO_FIELD)

    def click_call_taxi(self):
        self._click(self.CALL_A_TAXI_BUTTON)

    def select_comfort(self):
        comfort = self._find(self.COMFORT_CARD)

        if "active" not in comfort.get_attribute("class"):
            comfort.click()

    def comfort_is_selected(self):
        comfort = self._find(self.COMFORT_CARD)
        return "active" in comfort.get_attribute("class")

    def set_phone(self, phone_number):
        self._click(self.PHONE_NUMBER_BUTTON)
        self._type(self.PHONE_INPUT, phone_number)
        self._click(self.NEXT_BUTTON)

        phone_code = retrieve_phone_code(self.driver)

        self._type(self.CODE_INPUT, phone_code)
        self._click(self.CONFIRM_BUTTON)

    def get_inserted_phone_number(self):
        return self._get_text(self.INSERTED_PHONE_NUMBER)

    def set_card(self, card_number, card_code):
        self._click(self.PAYMENT_METHOD_BUTTON)
        self._click(self.ADD_CARD_BUTTON_ROW)
        self._type(self.CARD_NUMBER_INPUT, card_number)
        self._type(self.CARD_CODE_INPUT, card_code)
        self._press_tab()
        self._click(self.ADD_CARD_BUTTON)

    def get_current_payment_method(self):
        return self._get_text(self.CURRENT_PAYMENT_METHOD)

    def close_payment_method(self):
        self._click(self.CLOSE_PAYMENT_BUTTON)

    def set_driver_comment(self, comment):
        self._type(self.COMMENT_INPUT, comment)

    def get_driver_comment(self):
        return self._get_value(self.COMMENT_INPUT)

    def click_blanket_and_tissues(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BLANKET_SWITCH)
        ).click()

    def blanket_and_tissues_selected(self):
        return self._find(self.BLANKET_CHECKBOX).is_selected()

    def click_ice_cream_plus(self):
        self._click(self.ICE_CREAM_PLUS)

    def get_ice_cream_count(self):
        return self._get_text(self.ICE_CREAM_COUNT)

    def click_order_button(self):
        self._click(self.ORDER_BUTTON)

    def car_search_modal_is_displayed(self):
        return self._find(self.CAR_SEARCH_MODAL).is_displayed()
    def close_payment_method(self):
        self._click(self.CLOSE_PAYMENT_BUTTON)

    def set_driver_comment(self, comment):
        self._type(self.COMMENT_INPUT, comment)

    def get_driver_comment(self):
        return self._get_value(self.COMMENT_INPUT)

    def click_blanket_and_tissues(self):
        self.wait.until(EC.element_to_be_clickable(self.BLANKET_SWITCH)).click()

    def blanket_and_tissues_selected(self):
        return self._find(self.BLANKET_CHECKBOX).is_selected()

    def click_ice_cream_plus(self):
        self._click(self.ICE_CREAM_PLUS)

    def get_ice_cream_count(self):
        return self._get_text(self.ICE_CREAM_COUNT)

    def click_order_button(self):
        self._click(self.ORDER_BUTTON)

    def car_search_modal_is_displayed(self):
        return self._find(self.CAR_SEARCH_MODAL).is_displayed()