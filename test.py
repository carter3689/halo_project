from app import app
import unittest
from werkzeug.security import generate_password_hash, check_password_hash


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
        hashed = generate_password_hash('testing2', method='sha256')
        response = tester.post('/login',data= dict(username = 'bigtest', password = 'testing2'), follow_redirects = True)
        self.assertIn(b'Section title', response.data)
    # Ensure Login behaves correctly given the incorrect credentials
    # Ensure Logout behaves correctly given the correct credentials




if __name__ == '__main__':
    unittest.main()