import requests
import json
import allure
import pytest

base_url = "https://fakerestapi.azurewebsites.net"
Get_Url = "/api/v1/Users"
header = {'x-api-key': 'reqres-free-v1'}

@allure.feature("User Management API")
class TestUserManagement:

    def get_response(self):
        Get_url_link=base_url+Get_Url
        response = requests.get(Get_url_link)
        json_data=response.json()
        assert response.status_code == 200
        json_format = json.dumps(json_data, indent=4)
        print("Get has been successfully done")
        print( "Json response is " ,json_format)
        print("your getting response as ",response.status_code,"all details are present and okay")
        return response

def post_response():
    url=base_url+Get_Url
    body={
        "username": "tsest",
        "email": "tvsd@x.com",
        "password": "123456"
    }
    response = requests.post(url, json=body,headers=header)
    # assert response.status_code == 200
    json_data = response.json()
    user_id = json_data["id"]
    json_format = json.dumps(json_data, indent=4)
    print("Data has update with :", json_data ,"with user id :", user_id)
    print( "Json response is " ,json_format)
    assert json_data["id"]  == user_id
    print(response.status_code)
    print("New Data has been successfully done with server response as ",response.status_code)
    return user_id

def getuser_response(user_id):
    url=base_url+Get_Url+f"/{user_id}"
    response = requests.get(url)
    json_data=response.json()
    assert response.status_code == 404
    json_format = json.dumps(json_data, indent=4)
    print("Get has been successfully done")
    print( "Json response is " ,json_format)
    print("your getting a response ",response.status_code,"as NOT Found because the user id is not present :",user_id)
    return response

def put_response(user_id):
    url=base_url+Get_Url+f"/{user_id}"
    body={
        "userName": "Tommandjerry34"

    }
    response = requests.put(url, json=body)
    json_data = response.json()
    json_format = json.dumps(json_data, indent=4)
    print("Data has update with :", json_data)
    print( "Json response is " ,json_format)
    print(response.status_code)
    name=json_data["userName"]
    print(name)
    return response

def delete_response(user_id):
    url=base_url+Get_Url+f"/{user_id}"
    responses= requests.delete(url)
    print("Data has been deleted with user id :",user_id)
    json_data=responses.json()
    response= responses.status_code
    print(response)
    print(json_data)



post_response()
# get_response(self)
userid=post_response()
getuser_response(userid)
put_response(userid)
delete_response(userid)

