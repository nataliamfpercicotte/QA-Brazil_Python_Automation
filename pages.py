from html.parser import commentclose

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class UrbanRoutesPage:

        #De e Para

        from_campo = (By.ID, 'from')
        to_campo = (By.ID, 'to')

        #Chamar um táxi

        call_taxi_button = (
            By.XPATH,
            "//button[contains(text(),'Chamar um táxi')]"
        )

        comfort_button = (
            By.XPATH,
            "//div[@class='tcard-title' and text()='Comfort']/.."
        )

        #Inserir número de telefone

        phone_number_button = (
            By.XPATH,
            "//div[text()='Número de telefone']"
        )

        phone_input = (
            By.ID,
            "phone"
        )

        next_button = (
            By.XPATH,
            "//button[text()='Próximo']"
        )

        code_input = (
            By.ID,
            "code"
        )

        confirm_button = (
            By.XPATH,
            "//button[text()='Confirmar']"
        )

        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

        #Métodos COR POM

        def _find(self,locator):
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )

        def _click(self,locator):
            self.wait.until(
                EC.element_to_be_clickable(locator)
            ).click()

        def _type(self, locator, text):
            element = self._find(locator)
            element.clear()
            element.send_keys(text)

        #Endereço

        def _get_text(self,locator):
            return self._find(locator).text

        def _get_value(self,locator):
            return self._find(locator).get_attribute('value')

        def enter_locations(self, from_text, to_text):
            self._type(self.from_campo, from_text)
            self._type(self.to_campo, to_text)

        def get_from_location(self):
            return self._get_value(self.from_campo)

        def get_to_location(self):
            return self._get_value(self.to_campo)

        #Selecionar comfort

        def click_call_taxi(self):
            self._click(self.call_taxi_button)

        def select_comfort(self):
            comfort = self._find(self.comfort_button)

            if "active" not in comfort.get_attribute("class"):
                comfort.click()

        def comfort_is_selected(self):
            comfort = self._find(self.comfort_button)
            return "active" in comfort.get_attribute("class")

        #Numéro de telefone

        def click_phone_number(self):
            self._click(self.phone_number_button)

        def set_phone_number(self, phone):
            self._type(self.phone_input, phone)

        def click_next(self):
            self._click(self.next_button)

        def set_sms_code(self, code):
            self._type(self.code_input, code)

        def click_confirm(self):
            self._click(self.confirm_button)