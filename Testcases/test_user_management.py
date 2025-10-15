import pytest
import allure
from api.user_api import UserAPI
from common.test_data_generator import generate_user_data, generate_updated_email

@allure.feature("User Management API")
class TestUserManagement:

    @pytest.fixture(scope="function")
    def user_fixture(self):
        """A fixture to create a user for tests and clean up afterward."""
        api_client = UserAPI()
        created_users = []

        def _create_user():
            # Create a user and store its ID for cleanup
            user_data = generate_user_data()
            response = api_client.create_user(user_data)
            assert response.status_code == 200, "Fixture setup failed: Could not create user"
            user_id = response.json()['data']['id']
            created_users.append(user_id)
            return user_id, user_data

        yield _create_user

        # Teardown: Clean up all created users
        print("\n--- Cleaning up created users ---")
        for user_id in created_users:
            api_client.delete_user(user_id)
            print(f"Deleted user with ID: {user_id}")

    @allure.story("Create User")
    @allure.title("Test successful user creation (Positive Case)")
    def test_create_user_success(self, user_fixture):
        api_client = UserAPI()
        user_id, user_data = user_fixture() # Use the fixture to create a user

        with allure.step("Verify user details after creation"):
            get_response = api_client.get_user(user_id)
            assert get_response.status_code == 200
            response_json = get_response.json()
            assert response_json['data']['username'] == user_data['username']
            assert response_json['data']['email'] == user_data['email']

    @allure.story("Create User")
    @allure.title("Test creating a user with a missing email (Abnormal Case)")
    def test_create_user_missing_email(self):
        api_client = UserAPI()
        user_data = generate_user_data()
        del user_data['email']  # Remove the email field

        response = api_client.create_user(user_data)

        assert response.status_code == 400  # Assuming 400 for bad request
        assert "email is required" in response.json()['msg'].lower()

    @allure.story("Delete User")
    @allure.title("Test deleting a non-existent user (Abnormal Case)")
    def test_delete_non_existent_user(self):
        api_client = UserAPI()
        non_existent_id = 99999999

        response = api_client.delete_user(non_existent_id)

        assert response.status_code == 404 # Assuming 404 for not found
        assert "user not found" in response.json()['msg'].lower()

    @allure.story("Update User")
    @allure.title("Test updating a deleted user's email (Abnormal Case)")
    def test_update_deleted_user(self, user_fixture):
        api_client = UserAPI()
        user_id, _ = user_fixture()

        # First, delete the user
        with allure.step("Delete the user"):
            delete_response = api_client.delete_user(user_id)
            assert delete_response.status_code == 200

        # Now, try to update the deleted user
        with allure.step("Attempt to update the deleted user"):
            update_payload = generate_updated_email()
            update_response = api_client.update_user_email(user_id, update_payload)
            assert update_response.status_code == 404 # Should be "not found"