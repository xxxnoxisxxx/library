from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.contrib.auth.models import User

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
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(3)
		self.assertIn('Login Page', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h2').text 
		self.assertIn('Library', header_text)

	def test_can_login(self):
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(3)
		self.assertIn('Login Page', self.browser.title)
		username = self.browser.find_element_by_name('username')
		password = self.browser.find_element_by_name('password')

		username.send_keys("admin")
		password.send_keys("admin123")

		self.browser.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

		self.assertIn('Main Page', self.browser.title)

	def test_user_has_not_access_to_add_book(self):
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(3)
		self.assertIn('Login Page', self.browser.title)
		username = self.browser.find_element_by_name('username')
		password = self.browser.find_element_by_name('password')

		username.send_keys("test")
		password.send_keys("test")

		self.browser.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

		self.browser.get('http://localhost:8000/books/add_book')
		self.browser.implicitly_wait(3)
		self.assertIn('Django site admin', self.browser.title)

	def test_user_has_not_access_to_update_list_book(self):
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(3)
		self.assertIn('Login Page', self.browser.title)
		username = self.browser.find_element_by_name('username')
		password = self.browser.find_element_by_name('password')

		username.send_keys("test")
		password.send_keys("test")

		self.browser.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

		self.browser.get('http://localhost:8000/books/edit_book')
		self.browser.implicitly_wait(3)
		self.assertIn('Django site admin', self.browser.title)

	def test_user_has_not_access_to_update_book(self):
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(3)
		self.assertIn('Login Page', self.browser.title)
		username = self.browser.find_element_by_name('username')
		password = self.browser.find_element_by_name('password')

		username.send_keys("test")
		password.send_keys("test")

		self.browser.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

		self.browser.get('http://localhost:8000/books/edit_book/1')
		self.browser.implicitly_wait(3)
		self.assertIn('Django site admin', self.browser.title)

	def test_user_has_not_access_to_check_list_user(self):
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(3)
		self.assertIn('Login Page', self.browser.title)
		username = self.browser.find_element_by_name('username')
		password = self.browser.find_element_by_name('password')

		username.send_keys("test")
		password.send_keys("test")

		self.browser.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

		self.browser.get('http://localhost:8000/account/user/')
		self.browser.implicitly_wait(3)
		self.assertIn('Django site admin', self.browser.title)

	def test_user_has_not_access_to_check_other_user(self):
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(3)
		self.assertIn('Login Page', self.browser.title)
		username = self.browser.find_element_by_name('username')
		password = self.browser.find_element_by_name('password')

		username.send_keys("test")
		password.send_keys("test")

		self.browser.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

		self.browser.get('http://localhost:8000/account/user/test/')
		self.browser.implicitly_wait(3)
		self.assertIn('Django site admin', self.browser.title)