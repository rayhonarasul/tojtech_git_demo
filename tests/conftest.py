import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class") #scope=class means the fixture will run once for the entire test class, not once for every test method
def setup(request): #request is a built-in object that is used to configure the project, provides useful info
    option = Options()
    option.add_experimental_option("detach", True)
    option.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.implicitly_wait(15)
    driver.get("http://staging.shopping.beeyor.com/shop")
    request.cls.driver = driver #request allows to create customized properties , cls stands for class
    #the above line is responsible for setting the driver's configurations on the class level then pass it to fixture
    yield #pytest pauses the fixture and runs your tests, separates the setup code from teardown code
    driver.quit()
    #above is teardown method