import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to the Song Recommender</h1>', response.data)

    def test_recommendations(self):
        response = self.app.post('/recommendations', data=dict(song='Stay'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Here are 10 songs similar to Stay:</h2>', response.data)

if __name__ == '__main__':
    unittest.main()
