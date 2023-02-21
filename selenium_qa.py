import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

    # test_check_detail_barang - check detail barang
    def test_check_detail_barang(self):
        # login
        driver = self.browser #buka web browser
        self.test_a_success_login()

        driver.find_element(By.ID, "item_4_title_link").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"inventory_details_price").text
        self.assertIn('$29.99', response_data)

    # test_b_succes_login  - web http://barru.pythonanywhere.com/daftar
    def test_b_succes_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.ID,"email").send_keys("faris12345@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("faris12345") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"swal2-title").text
        self.assertIn('Welcome faris12345', response_data)

    # test_c_failed_register - failed register since data already exist
    def test_c_failed_register(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)

        # switch to signup
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)

        driver.find_element(By.ID,"name_register").send_keys("faris12345") # isi name
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("faris12345@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("faris12345") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"swal2-html-container").text
        self.assertIn('Gagal Register!', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()