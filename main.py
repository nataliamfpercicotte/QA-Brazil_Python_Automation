import time
import data
import helpers

from pages import UrbanRoutesPage as UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def _start_comfort_caminho(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_set_route(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO
        time.sleep(10)

    def test_select_plan(self):
        self._start_comfort_caminho()
        self.page.click_call_taxi()
        self.page.select_comfort()
        assert self.page.comfort_is_selected()
        time.sleep(10)

    def test_fill_phone_number(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_phone_number()
        self.page.set_phone_number(data.PHONE_NUMBER)
        self.page.click_next()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.set_sms_code(code)
        self.page.click_confirm()

        time.sleep(3)

    def test_fill_card(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_payment_method()
        self.page.click_add_card()

        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)

        self.page.click_add_button()
        time.sleep(5)

    def test_comment_for_driver(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_add_button()
        self.page.close_payment_method()

        self.page.set_driver_comment(data.MESSAGE_FOR_DRIVER)

        assert self.page.get_driver_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_add_button()
        self.page.close_payment_method()

        self.page.set_driver_comment(data.MESSAGE_FOR_DRIVER)
        time.sleep(3)

        self.page.click_blanket_and_tissues()
        time.sleep(5)

        assert self.page.blanket_and_tissues_selected()

    def test_order_2_ice_creams(self):
        for i in range(2):
         # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
            pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
