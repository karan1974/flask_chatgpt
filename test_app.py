import unittest
from flask import Flask
from app import app, get_chatgpt_response

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ChatGPT Web Application", response.data)

    def test_results_page(self):
        response = self.app.post('/results', data={'message': 'What is the capital of india'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You asked:", response.data)
        self.assertIn(b"The answer is:", response.data)

    def test_get_chatgpt_response(self):
        prompt = "What is the capital of india"
        response = get_chatgpt_response(prompt)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

if __name__ == '__main__':
    unittest.main()
