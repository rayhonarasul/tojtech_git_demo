from selenium.webdriver.common.by import By
from time import sleep

from page_objects.shop_page import ShopPage


class BaseClass:
    pass


class TestEndToEnd(BaseClass):
    def test_end_to_end(self):
        shop_page = ShopPage(self.driver)
        shop_page.get_add_to_cart().click() #.click here is a setter, it performs an action with the address of locator the getter returns
        self.driver.find_element(By.CSS_SELECTOR, "#components-form-token-input-0").send_keys("Albania") #send keys gives us the ability to type in an input in field

        list_of_countries = self.driver.find_elements(By.CSS_SELECTOR, "#components-form-token-field_-suggestion")
        for country in list_of_countries:
            if country.text == "Albania":
                country.click()
                break

        frame_element = self.driver.find_elements(By.TAG_NAME, "iframe") #find frame
        self.driver.switch_to.frame(frame_element[1]) #switch to frame
        self.driver.find_element(By.CSS_SELECTOR, "#Field-numberInput").send_keys("4242") #input number into card number box
        self.driver.switch_to.default_content() #switch out of the frame
        self.driver.find_element(By.XPATH, "//span[text()='Place Order']").click()
        print("This is a newly created message for git session.")
        print("New changes by American guy.")