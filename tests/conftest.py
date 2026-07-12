import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None #usually this none is used when you're creating an object without any value yet, you can assign values later on like line 17

def pytest_addoption(parser): #this allows to create custom arguments, for browsers, environments etc
    #parser is a parameter that will help us to pass/parse the customized arguments that we'll create; translate it to the system
    parser.addoption("--browser-name", action="store", default="chrome")
    #with above lines you can switch between environments and browsers

@pytest.fixture(scope="class") # scope = class means create the browser once for the entire test class, the browser opens once and closes after all tests finish
def setup(request):
    global driver
    option = Options()
    option.add_experimental_option("detach", True)
    browser_name = request.config.getoption("--browser-name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://staging.shopping.beeyor.com/shop")
    request.cls.driver = driver #take the browser we just created and give it to this entire test class so that every test method can access it through self.driver
    yield
    driver.quit()