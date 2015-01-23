# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 21:38:31 2015

@author: raoul
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class MallampatiTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8051")

    def test_title(self):
        self.assertIn("Mallampati", self.driver.title)
        
    def test_page_header(self):
        content = self.driver.find_element_by_class_name("jumbotron")
        self.assertIn("Welcome", content.text)
        
    def test_form_exists(self):
        self.driver.get("http://127.0.0.1:8051/photobooth")
        try:
            self.form = self.driver.find_element_by_class_name("form-group")
            self.exists = True
        except NoSuchElementException:
            self.exists = False
        self.assertTrue(self.exists)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



