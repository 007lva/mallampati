# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 21:38:31 2015

@author: raoul
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from detect_platform import detect_platform

class HomepageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8051")

    def test_title(self):
        self.assertIn("Mallampati", self.driver.title)
        
    def test_page_header(self):
        self.content = self.driver.find_element_by_class_name("jumbotron")
        self.assertIn("Welcome", self.content.text)
        
    def tearDown(self):
        self.driver.close()
        

class PhotoboothpageTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8051/photobooth")
        
    def test_form_exists(self):
        try:
            self.form = self.driver.find_element_by_class_name("form-group")
            self.exists = True
        except NoSuchElementException:
            self.exists = False
        self.assertTrue(self.exists)
        
    def test_webcamphotobooth_if_desktop(self):
        from MallampatiPhotobooth import app
        with app.test_request_context():  # required to get context locals
            self.is_mobile = detect_platform.os_platform_not_desktop()
            if self.is_mobile == False:
                self.assertTrue(self.driver.find_element_by_id("my_camera"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



