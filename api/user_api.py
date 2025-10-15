import requests
import allure
from common.config_handler import config

class UserAPI:
    """A client to interact with the User Management API."""

    def __init__(self):
        self.base_url = config['base_url']
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def _make_request(self, method, endpoint, **kwargs):
        """A private helper method to make requests and attach details to Allure reports."""
        url = f"{self.base_url}{endpoint}"

        with allure.step(f"{method.upper()} {url}"):
            response = self.session.request(method, url, timeout=config['timeout'], **kwargs)

            # Attach request details to Allure report
            allure.attach(f"Request URL: {response.request.url}", name="Request URL")
            if response.request.body:
                allure.attach(response.request.body, name="Request Body", attachment_type=allure.attachment_type.JSON)

            # Attach response details to Allure report
            allure.attach(f"Status Code: {response.status_code}", name="Response Status Code")
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)

        return response

    def create_user(self, payload):
        return self._make_request('POST', '/users', json=payload)

    def get_user(self, user_id):
        return self._make_request('GET', f'/users/{user_id}')

    def update_user_email(self, user_id, payload):
        return self._make_request('PUT', f'/users/{user_id}', json=payload)

    def delete_user(self, user_id):
        return self._make_request('DELETE', f'/users/{user_id}')

    def batch_query_users(self, params=None):
        return self._make_request('GET', '/users', params=params)