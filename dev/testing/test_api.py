import requests

class APITester:
    def __init__(self, base_url):
        self.base_url = base_url

    def test_create_user(self, username, email, password):
        url = f"{self.base_url}/create_user"
        data = {
            'username': username,
            'email': email,
            'password': password
        }
        response = requests.post(url, json=data)
        return response

    def test_get_users(self):
        url = f"{self.base_url}/get_users"
        response = requests.get(url)
        return response

# Example usage:
if __name__ == "__main__":
    tester = APITester("http://localhost:5000")
    
    # Test the create_user API
    response_create_user = tester.test_create_user("test_user3", "test3@example.com", "password123")
    print("Create User - Response status code:", response_create_user.status_code)
    print("Create User - Response content:", response_create_user.json())

    response_create_user = tester.test_create_user("test_user4", "test4@example.com", "password456")
    print("Create User - Response status code:", response_create_user.status_code)
    print("Create User - Response content:", response_create_user.json())
    
    # Test the get_users API
    response_get_users = tester.test_get_users()
    print("Get Users - Response status code:", response_get_users.status_code)
    print("Get Users - Response content:", response_get_users.json())
