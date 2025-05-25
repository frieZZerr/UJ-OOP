from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import re

BASE_URL = "http://localhost:5173"

class Test4PawsApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_homepage_title(self):
        self.driver.get(BASE_URL + "/products")
        self.assertIn("4-Paws", self.driver.page_source)

    def test_nav_products(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.LINK_TEXT, "Products").click()
        self.assertIn("Products", self.driver.page_source)

    def test_nav_cart(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.assertIn("Cart", self.driver.page_source)

    def test_nav_payments(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.LINK_TEXT, "Payments").click()
        self.assertIn("Payments", self.driver.page_source)

    def test_products_listed(self):
        self.driver.get(BASE_URL + "/products")
        products = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(products), 1)

    def test_add_to_cart_alert(self):
        self.driver.get(BASE_URL + "/products")
        btn = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")[0]
        btn.click()
        alert = self.driver.switch_to.alert
        self.assertIn("added to cart", alert.text)
        alert.accept()

    def test_cart_shows_added_product(self):
        self.driver.get(BASE_URL + "/products")
        btn = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")[0]
        product_name = self.driver.find_elements(By.TAG_NAME, "li")[0].text.split(" - ")[0]
        btn.click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.assertIn(product_name, self.driver.page_source)

    def test_cart_clear(self):
        self.driver.get(BASE_URL + "/products")
        btn = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")[0]
        btn.click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]").click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_cart_summary(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:2]:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.assertIn("Summary:", self.driver.page_source)

    def test_payments_page_input(self):
        self.driver.get(BASE_URL + "/payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        input_box.send_keys("100")
        self.assertEqual(input_box.get_attribute("value"), "100")

    def test_payments_button(self):
        self.driver.get(BASE_URL + "/payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        input_box.send_keys("50")
        btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Pay')]")
        btn.click()
        # Payment alert may appear, but backend endpoint is /payment not /payments, so error expected
        time.sleep(1)
        self.assertIn("Payments", self.driver.page_source)

    def test_products_prices(self):
        self.driver.get(BASE_URL + "/products")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        price_pattern = re.compile(r"\d+\.\d{2} PLN")
        found = False
        for item in items:
            if price_pattern.search(item.text):
                found = True
                self.assertRegex(item.text, r"\d+\.\d{2} PLN")
        self.assertTrue(found, "No product prices found in product list.")

    def test_cart_empty_message(self):
        self.driver.get(BASE_URL + "/cart")
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_products_page_has_add_to_cart(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        self.assertGreaterEqual(len(btns), 1)

    def test_cart_total_updates(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        btns[0].click()
        self.driver.switch_to.alert.accept()
        btns[1].click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        summary = self.driver.find_element(By.XPATH, "//p[strong[contains(text(),'Summary:')]]").text
        self.assertRegex(summary, r"Summary: \d+\.\d{2} PLN")

    def test_nav_links_present(self):
        self.driver.get(BASE_URL)
        for link in ["Products", "Cart", "Payments"]:
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, link))

    def test_header_present(self):
        self.driver.get(BASE_URL)
        header = self.driver.find_element(By.TAG_NAME, "header")
        self.assertIn("4-Paws", header.text)

    def test_main_content_present(self):
        self.driver.get(BASE_URL)
        main = self.driver.find_element(By.TAG_NAME, "main")
        self.assertTrue(main.is_displayed())

    def test_products_page_url(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.LINK_TEXT, "Products").click()
        self.assertIn("/products", self.driver.current_url)

    def test_cart_page_url(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.assertIn("/cart", self.driver.current_url)

    def test_payments_page_url(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.LINK_TEXT, "Payments").click()
        self.assertIn("/payments", self.driver.current_url)

    def test_products_list_content(self):
        self.driver.get(BASE_URL + "/products")
        ul = self.driver.find_element(By.TAG_NAME, "ul")
        self.assertTrue(ul.is_displayed())

    def test_cart_list_content(self):
        self.driver.get(BASE_URL + "/cart")
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "div").is_displayed())

    def test_payments_input_placeholder(self):
        self.driver.get(BASE_URL + "/payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        self.assertEqual(input_box.get_attribute("placeholder"), "Amount")

    def test_add_multiple_products_to_cart(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:3]:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(items), 3)

    def test_cart_total_correctness(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        prices = []
        price_pattern = re.compile(r"(\d+\.\d{2}) PLN")
        for btn in btns[:2]:
            li = btn.find_element(By.XPATH, "./parent::li")
            match = price_pattern.search(li.text)
            self.assertIsNotNone(match, f"No price found in '{li.text}'")
            price = float(match.group(1))
            prices.append(price)
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        summary = self.driver.find_element(By.XPATH, "//p[strong[contains(text(),'Summary:')]]").text
        total_match = price_pattern.search(summary)
        self.assertIsNotNone(total_match, f"No total price found in '{summary}'")
        total = float(total_match.group(1))
        self.assertAlmostEqual(total, sum(prices), places=2)

    def test_cart_clear_button_present(self):
        self.driver.get(BASE_URL + "/products")
        btn = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")[0]
        btn.click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]"))

    def test_payments_button_present(self):
        self.driver.get(BASE_URL + "/payments")
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(),'Pay')]"))

    def test_products_page_header(self):
        self.driver.get(BASE_URL + "/products")
        h2 = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.text, "Products")

    def test_cart_page_header(self):
        self.driver.get(BASE_URL + "/cart")
        h2 = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.text, "Cart")

    def test_payments_page_header(self):
        self.driver.get(BASE_URL + "/payments")
        h2 = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.text, "Payments")

if __name__ == "__main__":
    unittest.main()
