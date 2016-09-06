from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#class NewVisitorTest(LiveServerTestCase):
class NewVisitorTest(TestCase):
	"""docstring for NewVisitorTest"""
	fixtures = ['books/fixtures/initial_data.json']

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_to_login_page(self):
		#self.browser.get(self.live_server_url)
		self.browser.get('http://localhost:8000/')
		self.assertIn('Login Page', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h2').text 
		self.assertIn('Library', header_text)

	def test_can_login(self):
		self.browser.get('http://localhost:8000/')
		self.assertIn('Login Page', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h2').text 
		self.assertIn('Library', header_text)