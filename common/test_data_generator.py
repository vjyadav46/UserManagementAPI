from faker import Faker

# Initialize the Faker instance
fake = Faker()

def generate_user_data():
    """Generates a dictionary with random user data."""
    username = fake.user_name() + str(fake.random_int(min=100, max=999))
    email = fake.email()
    password = fake.password(length=12)
    return {
        "username": username,
        "email": email,
        "password": password
    }

def generate_updated_email():
    """Generates a new random email for update tests."""
    return {"email": fake.email()}