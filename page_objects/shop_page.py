#This is a page object file.

from selenium.webdriver.common.by import By

#self.driver.find_element(By.XPATH, "//span[text()='Add to cart'])[1]").click()
#self.driver.find_element(By.CLASS_NAME, "wc-block-mini-cart__button ").click()
#self.driver.find_element(By.XPATH, "//span[text()= 'Go to checkout']").click()

class ShopPage:
    add_to_cart = (By.XPATH, "//span[text()='Add to cart'])[1]") #these are class variables
    cart_button = (By.CLASS_NAME, "wc-block-mini-cart__button ")
    go_to_checkout = (By.XPATH, "//span[text()= 'Go to checkout']")


    def __init__(self, driver):
        self.driver = driver #this is just a local instance variable named driver, not the actual driver



    #methods that are responsible to locate above elements in the domtree, called getters which are lower implementations
    def get_add_to_cart(self):
        return self.driver.find_element(*ShopPage.add_to_cart) #whenever the getter is used it will return the actual element/locator back
        #the self here is the get_add_to_cart object so it takes driver and passes it to actual getter
