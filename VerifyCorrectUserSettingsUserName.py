import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\katya\OneDrive\Документы\chromedriver.exe")
        cls.driver.get("http://localhost:53326/")
        cls.driver.implicitly_wait(10)

    def test_open_event_express(self):
        driver = self.driver
        sign_in = driver.find_element_by_class_name('MuiButton-label').click()
        email = driver.find_element_by_name("email").send_keys("user@gmail.com")
        password = driver.find_element_by_name("password")
        password.send_keys("1qaz1qaz")
        password.send_keys(Keys.ENTER)
        username = driver.find_element_by_xpath("//div[@class = 'd-flex flex-column align-items-center']/h4").text
        self.assertEqual("UserTest", username)

    def test_open_settings_page(self):
        driver = self.driver
        home = driver.find_element_by_xpath("//div/a[@href='/profile']/button").click()

    def test_verify_changing_username(self):
        driver = self.driver
        change_username = driver.find_elements_by_id("panel1bh-header")[1].click()
        change_username_input = driver.find_element_by_name("UserName")
        change_username_input.send_keys("1")
        change_username_input.send_keys(Keys.ENTER)
        success = driver.find_element_by_id("client-snackbar").text
        self.assertEqual("Username is changed", success)


    @classmethod
    def tearDownClass(cls):
        cls.driver.refresh()
        change_username = cls.driver.find_elements_by_id("panel1bh-header")[1].click()
        change_username_input = cls.driver.find_element_by_name("UserName")
        change_username_input.send_keys("UserTest")
        change_username_input.send_keys(Keys.ENTER)
        cls.driver.close()
        pass


if __name__ == '__main__':
    unittest.main()
