from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
	"""docstring for NewVisitorTest"""

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	
	def test_can_start_a_list_and_retrieve_it_later(self):

		self.browser.get(self.live_server_url)
		
		self.assertIn('Login', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h2').text 
		self.assertIn('Library', header_text)