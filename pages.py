from html.parser import commentclose

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys


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

        #Inserir cartão de crédito

        payment_method = (
            By.CLASS_NAME,
            "pp-text"
        )

        add_card = (
            By.XPATH,
            "//div[contains(@class, 'pp-row') and .//div[text()='Adicionar cartão']]"
        )

        card_number = (
            By.CSS_SELECTOR,
            "input.card-input#number"
        )

        card_code = (
            By.CSS_SELECTOR,
            "input.card-input#code"
        )

        add_card_button = (
            By.XPATH,
            "//button[text()='Adicionar']"
        )

        #Comentário

        close_payment_button = (
            By.XPATH,
            "//div[contains(@class,'payment-picker') and contains(@class,'open')]//button[contains(@class,'section-close')]"
        )

        comment_input = (
            By.ID,
            "comment"
        )

        #Cobertores e lenços

        blanket_switch = (
            By.XPATH,
            "//div[text()='Cobertor e lençóis']/following::span[@class='slider round'][1]"
        )

        blanket_checkbox = (
            By.XPATH,
            "//div[text()='Cobertor e lençóis']/following::input[@type='checkbox'][1]"
        )


        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

        #Métodos COR POM

        def _find(self,locator):
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )

        def _click(self, locator):
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.execute_script("arguments[0].click();", element)

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

        #Cartão de crédito

        def click_payment_method(self):
            self._click(self.payment_method)

        def click_add_card(self):
            self._click(self.add_card)

        def set_card_number(self, number):
            self._type(self.card_number, number)

        def set_card_code(self, code):
            element = self.wait.until(
                EC.element_to_be_clickable(self.card_code)
            )
            element.click()
            element.send_keys(code)
            element.send_keys(Keys.TAB)

        def click_add_button(self):
            self._click(self.add_card_button)

        #Comentário para o motorista

        def close_payment_method(self):
            self._click(self.close_payment_button)

        def set_driver_comment(self, comment):
            self._type(self.comment_input, comment)

        def get_driver_comment(self):
            return self._get_value(self.comment_input)

        #Solicitar cobertores e lenços

        def click_blanket_and_tissues(self):
            element = self._find(self.blanket_switch)

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )

            time.sleep(1)
            element.click()

        def blanket_and_tissues_selected(self):
            return self._find(self.blanket_checkbox).is_selected()