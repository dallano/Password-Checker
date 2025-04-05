## ***************************************************************************************
# The following program was written to give users more security when checking for
#   Leaked passwords. It takes in a list of passwords the user would like to check for,
#   and creates a utf-8 hash of the password. It then sends the first 5 digites of this
#   hash to an API. The said API then returns sets of the hashes that match
#   the sent query along with a count of how many times that password has been leaked.
#   This program then compares that with the remaining hash that wasn't sent and reports to the
#   user the amount of times their password has been leaked.
# 
# In order to check for leaked passwords, the user must modify the PASSWORDS list.
#   It is recommended that the user also delete their passwords from said list after
#   the program has finished to ensure optimal security.
#
#   Author: Dallan Atwood
## ***************************************************************************************
import requests
import hashlib
import sys

# Below is the list of passwords to check for data leaks.
PASSWORDS = [
    'password_to_check',
]

# Requests access to the given url
# query_char is the first 5 characters of a hashed password that is given to the URL.
#   This prioritizes security and prevents the password from being leaked any further
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error accessing the url, Request status: {res.status_code}, check the api and try again.')
    else:
        print('Successfully accessed API...')
        return res


# Data received is the tail end of the hash encryption and the # of times it was discovered
# We search for our matching hash and return the count.
def get_response_count(hashes, hash_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_check: # Search for a match with our password
            return count    # Return its count

    return 0 # Otherwise it wasn't discovered. Return 0!


# Convert password into a sh1 HASH object and further into hexidecimal string and convert to all uppercase
# This formatting is required by the API being used.
def pwned_api_check(password):
    sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_pass[:5], sha1_pass[5:]

    return get_response_count(request_api_data(first5_char), tail)


def main():
    for password in PASSWORDS:
        print(f'Password: {password} was discovered in {pwned_api_check(password)}, data leak(s).')

    return 'Process complete.'


if __name__ == '__main__':
    sys.exit(main())
