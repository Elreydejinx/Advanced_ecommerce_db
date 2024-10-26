import unittest.TestCase import TestCase

class TestAddEndpoint(unittest.TestCase):
    def setup(self):
        self.app = create_app()
        self.client = self.app.test.client
        self.add_url = 'http://localhost:8080'

    def test_add_endpoint(self):
        response = self.client.post(self.add_url, json={'a': 1, 'b': 2})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 3)
        self.assertEqual(data['message'], 'Addition successful')

    def test_add_endpoint_invalid_data(self):
        response = self.client.post(self.add_url, json={'a': '1', 'b': 2})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Invalid input data')
        self.assertEqual(data['error'], 'Invalid integer value for a')
        self.assertEqual(data['error'], 'Invalid integer value for b')

    def test_add_endpoint_missing_data(self):
        response = self.client.post(self.add_url, json={'a': 1})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Invalid input data')
        self.assertEqual(data['error'], 'Missing required field b')
    
    def test_add_endpoint_large_numbers(self):
        response = self.client.post(self.add_url, json={'a': 10**100, 'b': 10**100})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 2 * 10**100)
        self.assertEqual(data['message'], 'Addition successful')

    def test_add_endpoint_float_numbers(self):
        response = self.client.post(self.add_url, json={'a': 1.5, 'b': 2.5})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 4.0)
        self.assertEqual(data['message'], 'Addition successful')
    
    def test_add_endpoint_negative_numbers(self):
        response = self.client.post(self.add_url, json={'a': -1, 'b': -2})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], -3)
        self.assertEqual(data['message'], 'Addition successful')

    def test_add_endpoint_zero(self):
        response = self.client.post(self.add_url, json={'a': 0, 'b': 0})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 0)
        self.assertEqual(data['message'], 'Addition successful')

    def test_add_endpoint_custom_message(self):
        response = self.client.post(self.add_url, json={'a': 1, 'b': 2}, headers={'X-Custom-Message': 'Custom addition message'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 3)
        self.assertEqual(data['message'], 'Custom addition message')
        self.assertEqual(data['custom_message'], 'Custom addition message')

    def test_add_endpoint_large_numbers_custom_message(self):
        response = self.client.post(self.add_url, json={'a': 10**100, 'b': 10**100}, headers={'X-Custom-Message': 'Custom addition message'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 2 * 10**100)
        self.assertEqual(data['message'], 'Custom addition message')
        self.assertEqual(data['custom_message'], 'Custom addition message')

    def test_add_endpoint_float_numbers_custom_message(self):
        response = self.client.post(self.add_url, json={'a': 1.5, 'b': 2.5}, headers={'X-Custom-Message': 'Custom addition message'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 4.0)
        self.assertEqual(data['message'], 'Custom addition message')
        self.assertEqual(data['custom_message'], 'Custom addition message')