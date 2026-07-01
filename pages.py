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

