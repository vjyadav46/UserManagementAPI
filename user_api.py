import requests
from common.config_reader import ConfigReader
from common.logger import logger

class UserApi:
    def __init__(self):
        config = ConfigReader()
        self.base_url = config.get_base_url()
        self.headers = config.get_headers()

    def create_user(self, username, email, password):
        url = f"{self.base_url}/api/users"
        payload = {"username": username, "email": email, "password": password}
        logger.info(f"Creating user: {payload}")
        return requests.post(url, json=payload, headers=self.headers)

    def get_user(self, user_id):
        url = f"{self.base_url}/api/users/{user_id}"
        logger.info(f"Getting user with ID: {user_id}")
        return requests.get(url, headers=self.headers)

    def update_user_email(self, user_id, email):
        url = f"{self.base_url}/api/users/{user_id}"
        payload = {"email": email}
        logger.info(f"Updating user {user_id} email to: {email}")
        return requests.put(url, json=payload, headers=self.headers)

    def delete_user(self, user_id):
        url = f"{self.base_url}/api/users/{user_id}"
        logger.info(f"Deleting user with ID: {user_id}")
        return requests.delete(url, headers=self.headers)

    def batch_query_users(self, page=1, size=10, keyword=None):
        url = f"{self.base_url}/api/v1/users"
        params = {"page": page, "size": size}
        if keyword:
            params["keyword"] = keyword
        logger.info(f"Batch querying users with params: {params}")
        return requests.get(url, headers=self.headers, params=params)
