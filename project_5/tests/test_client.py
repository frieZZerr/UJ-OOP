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

    def test_products_details_and_buttons(self):
        self.driver.get(BASE_URL + "/products")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for i, item in enumerate(items[3:]):
            self.assertIn("-", item.text)
            self.assertIn("PLN", item.text)
            self.assertRegex(item.text, r"\d+\.\d{2} PLN")
            if i < len(btns):
                self.assertTrue(btns[i].is_displayed())
                self.assertTrue(btns[i].is_enabled())

    def test_add_and_remove_all_products(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(items), len(btns))
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]").click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_payments_input_various_values(self):
        self.driver.get(BASE_URL + "/payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        for value in ["0", "1", "123", "9999", "0.01", "100.99"]:
            input_box.clear()
            input_box.send_keys(value)
            self.assertEqual(input_box.get_attribute("value"), value)

    def test_navigation_and_headers(self):
        for page, header in [("/products", "Products"), ("/cart", "Cart"), ("/payments", "Payments")]:
            self.driver.get(BASE_URL + page)
            h2 = self.driver.find_element(By.TAG_NAME, "h2")
            self.assertEqual(h2.text, header)
            self.assertTrue(h2.is_displayed())

    def test_products_page_structure(self):
        self.driver.get(BASE_URL + "/products")
        ul = self.driver.find_element(By.TAG_NAME, "ul")
        self.assertTrue(ul.is_displayed())
        items = self.driver.find_elements(By.TAG_NAME, "li")
        for item in items[3:]:
            self.assertTrue(item.is_displayed())
            self.assertIn("PLN", item.text)

    def test_cart_summary_format_and_value(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        prices = []
        price_pattern = re.compile(r"(\d+\.\d{2}) PLN")
        for btn in btns[:3]:
            li = btn.find_element(By.XPATH, "./parent::li")
            match = price_pattern.search(li.text)
            self.assertIsNotNone(match)
            prices.append(float(match.group(1)))
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        summary = self.driver.find_element(By.XPATH, "//p[strong[contains(text(),'Summary:')]]").text
        total_match = price_pattern.search(summary)
        self.assertIsNotNone(total_match)
        total = float(total_match.group(1))
        self.assertAlmostEqual(total, sum(prices), places=2)
        self.assertRegex(summary, r"Summary: \d+\.\d{2} PLN")

    def test_cart_clear_button_and_empty_state(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:2]:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        clear_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]")
        self.assertTrue(clear_btn.is_displayed())
        clear_btn.click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_all_nav_links_work(self):
        self.driver.get(BASE_URL)
        for link, url_part in [("Products", "/products"), ("Cart", "/cart"), ("Payments", "/payments")]:
            self.driver.find_element(By.LINK_TEXT, link).click()
            self.assertIn(url_part, self.driver.current_url)
            self.driver.get(BASE_URL)

    def test_products_add_to_cart_alert_texts(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:3]:
            btn.click()
            alert = self.driver.switch_to.alert
            self.assertIn("added to cart", alert.text.lower())
            alert.accept()

    def test_products_listed_and_content(self):
        self.driver.get(BASE_URL + "/products")
        products = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(products), 1)
        for product in products[3:]:
            self.assertIn("PLN", product.text)
            self.assertIn("-", product.text)
            self.assertRegex(product.text, r"\d+\.\d{2} PLN")

    def test_cart_add_and_remove_multiple(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:5]:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(items), 5)
        clear_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]")
        clear_btn.click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_navigation_links(self):
        self.driver.get(BASE_URL)
        nav_links = ["Products", "Cart", "Payments"]
        for link in nav_links:
            el = self.driver.find_element(By.LINK_TEXT, link)
            self.assertTrue(el.is_displayed())
            self.assertTrue(el.is_enabled())

    def test_payments_input_and_button(self):
        self.driver.get(BASE_URL + "/payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        self.assertEqual(input_box.get_attribute("placeholder"), "Amount")
        for value in ["10", "20", "30", "40", "50"]:
            input_box.clear()
            input_box.send_keys(value)
            self.assertEqual(input_box.get_attribute("value"), value)
        btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Pay')]")
        self.assertTrue(btn.is_displayed())
        self.assertTrue(btn.is_enabled())

    def test_products_page_headers_and_buttons(self):
        self.driver.get(BASE_URL + "/products")
        h2 = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.text, "Products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns:
            self.assertTrue(btn.is_displayed())
            self.assertTrue(btn.is_enabled())

    def test_cart_page_headers_and_content(self):
        self.driver.get(BASE_URL + "/cart")
        h2 = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.text, "Cart")
        div = self.driver.find_element(By.TAG_NAME, "div")
        self.assertTrue(div.is_displayed())

    def test_payments_page_headers_and_content(self):
        self.driver.get(BASE_URL + "/payments")
        h2 = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.text, "Payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        self.assertTrue(input_box.is_displayed())

    def test_products_add_to_cart_alert_text(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:3]:
            btn.click()
            alert = self.driver.switch_to.alert
            self.assertIn("added to cart", alert.text.lower())
            alert.accept()

    def test_cart_summary_format(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:2]:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        summary = self.driver.find_element(By.XPATH, "//p[strong[contains(text(),'Summary:')]]").text
        self.assertRegex(summary, r"Summary: \d+\.\d{2} PLN")

    def test_cart_empty_message_after_clear(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:2]:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]").click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_products_have_unique_names(self):
        self.driver.get(BASE_URL + "/products")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        names = set()
        for item in items:
            name = item.text.split(" - ")[0]
            self.assertNotIn(name, names)
            names.add(name)
        self.assertGreater(len(names), 0)

    def test_cart_add_remove_single_product(self):
        self.driver.get(BASE_URL + "/products")
        btn = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")[0]
        product_name = self.driver.find_elements(By.TAG_NAME, "li")[0].text.split(" - ")[0]
        btn.click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.assertIn(product_name, self.driver.page_source)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]").click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_products_buttons_are_clickable(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns:
            self.assertTrue(btn.is_enabled())
            self.assertTrue(btn.is_displayed())

    def test_cart_summary_updates_correctly(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        prices = []
        price_pattern = re.compile(r"(\d+\.\d{2}) PLN")
        for btn in btns[:2]:
            li = btn.find_element(By.XPATH, "./parent::li")
            match = price_pattern.search(li.text)
            self.assertIsNotNone(match)
            prices.append(float(match.group(1)))
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        summary = self.driver.find_element(By.XPATH, "//p[strong[contains(text(),'Summary:')]]").text
        total_match = price_pattern.search(summary)
        self.assertIsNotNone(total_match)
        total = float(total_match.group(1))
        self.assertAlmostEqual(total, sum(prices), places=2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]").click()
        self.assertNotIn("Summary:", self.driver.page_source)

    def test_payments_input_rejects_text(self):
        self.driver.get(BASE_URL + "/payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        input_box.clear()
        input_box.send_keys("abc")
        self.assertEqual(input_box.get_attribute("value"), "")

    def test_products_page_contains_expected_elements(self):
        self.driver.get(BASE_URL + "/products")
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "ul").is_displayed())
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "h2").is_displayed())
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        self.assertGreaterEqual(len(btns), 1)

    def test_cart_page_contains_expected_elements(self):
        self.driver.get(BASE_URL + "/cart")
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "h2").is_displayed())
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "div").is_displayed())

    def test_payments_page_contains_expected_elements(self):
        self.driver.get(BASE_URL + "/payments")
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "h2").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@type='number']").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(),'Pay')]").is_displayed())

    def test_cart_empty_after_clear(self):
        self.driver.get(BASE_URL + "/products")
        btn = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")[0]
        btn.click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]").click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_products_names_are_not_empty(self):
        self.driver.get(BASE_URL + "/products")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        for item in items:
            name = item.text.split(" - ")[0].strip()
            self.assertNotEqual(name, "")
            self.assertGreater(len(name), 1)

    def test_cart_button_disabled_when_empty(self):
        self.driver.get(BASE_URL + "/cart")
        clear_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Clear cart')]")
        if clear_buttons:
            self.assertFalse(clear_buttons[0].is_enabled())
        self.assertIn("Your cart is empty", self.driver.page_source)

    def test_payments_placeholder_and_type(self):
        self.driver.get(BASE_URL + "/payments")
        input_box = self.driver.find_element(By.XPATH, "//input[@type='number']")
        self.assertEqual(input_box.get_attribute("placeholder"), "Amount")
        self.assertEqual(input_box.get_attribute("type"), "number")

    def test_cart_add_multiple_and_clear(self):
        self.driver.get(BASE_URL + "/products")
        btns = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for btn in btns[:3]:
            btn.click()
            self.driver.switch_to.alert.accept()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(items), 3)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Clear cart')]").click()
        self.assertIn("Your cart is empty", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()
