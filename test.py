from app import app
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import generate_csrf
from flask_csrf_test_client_config import FlaskClient_Config 

import os
import pytest


class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
    # Ensure that flask was set up correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertTrue(b'Please sign in' in response.data)

    # Ensure Login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',data= {"username":"bigtest", "password":"testing2"}, follow_redirects = True, content_type='application/x-www-form-urlencoded')
        self.assertIn(b'Section title', response.data)
    # Ensure Login behaves correctly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',data= {"username":"te", "password":"testing2"}, follow_redirects = True, content_type='application/x-www-form-urlencoded')
        self.assertIn(b'Invalid username or password', response.data)
    # Ensure Logout behaves correctly given the correct credentials
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.post('/logout', follow_redirects = True, content_type='application/x-www-form-urlencoded')
        self.assertIn(b'Please sign in', response.data)


if __name__ == '__main__':
    unittest.main()