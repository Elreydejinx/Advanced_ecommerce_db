from unittest import TestCase

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

    def TestLoginCustomer(unittest.TestCase):
        def setUp(self):
            self.app = create_app()
            self.client = self.app.test.client
            self.login_url = 'http://localhost:8080/login'
            self.customer_data = {'username': 'customer', 'password': 'password'}
            self.response = self.client.post(self.login_url, json=self.customer_data)
            self.token = json.loads(self.response.data)['token']
            self.headers = {'Authorization': f'Bearer {self.token}'}

        def test_login_customer(self):
            response = self.client.get('/customers', headers=self.headers)
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data['customers'])
            self.assertEqual(data['message'], 'Customers retrieved successfully')
            self.assertEqual(data['total_customers'], 1)
            self.assertEqual(data['page'], 1)
            self.assertEqual(data['per_page'], 10)
            self.assertEqual(data['total_pages'], 1)
            self.assertEqual(data['current_page'], 1)
            self.assertEqual(data['prev_page'], None)
            self.assertEqual(data['next_page'], None)
            self.assertEqual(data['first_page'], 1)
            self.assertEqual(data['last_page'], 1)
            self.assertEqual(data['from'], 1)

        def test_login_customer_invalid_token(self):
            headers = {'Authorization': 'Bearer invalid_token'}
            response = self.client.get('/customers', headers=headers)
            self.assertEqual(response.status_code, 401)
            data = json.loads(response.data)
            self.assertEqual(data['message'], 'Invalid token')
            self.assertEqual(data['error'], 'Missing Authorization header')
            self.assertEqual(data['error'], 'Invalid token')
            self.assertEqual(data['error'], 'Expired token')
            self.assertEqual(data['error'], 'Invalid audience')
            self.assertEqual(data['error'], 'Invalid issuer')
            self.assertEqual(data['error'], 'Missing required claims')
            self.assertEqual(data['error'], 'Invalid claim "jti"')
            self.assertEqual(data['error'], 'Invalid claim "iat"')
            self.assertEqual(data['error'], 'Invalid claim "nbf"')
            self.assertEqual(data['error'], 'Invalid claim "exp"')
            self.assertEqual(data['error'], 'Invalid claim "iat"')
            self.assertEqual(data['error'], 'Invalid claim "iss"')
            self.assertEqual(data['error'], 'Invalid claim "aud"')
            self.assertEqual(data['error'], 'Invalid claim "sub"')
            self.assertEqual(data['error'], 'Invalid claim "email"')
            self.assertEqual(data['error'], 'Invalid claim "name"')
            self.assertEqual(data['error'], 'Invalid claim "role"')
            self.assertEqual(data['error'], 'Invalid claim "iat"')
            self.assertEqual(data['error'], 'Invalid claim "exp"')
            self.assertEqual(data['error'], 'Invalid claim "iss"')
            self.assertEqual(data['error'], 'Invalid claim "aud"')
            self.assertEqual(data['error'], 'Invalid claim "sub"')
            self.assertEqual(data['error'], 'Invalid claim "email"')
            self.assertEqual(data['error'], 'Invalid claim "name"')
            self.assertEqual(data['error'], 'Invalid claim "role"')
            self.assertEqual(data['error'], 'Invalid claim "iat"')
            self.assertEqual(data['error'], 'Invalid claim "exp"')
            self.assertEqual(data['error'], 'Invalid claim "iss"')

            # Additional test cases for other errors if needed...
        @patch('django.db.models.fields.')
        