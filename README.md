# Password-Checker
Allows a user to securely check if their passwords have been detected in data breeches

## Instructions:
- First download main.py to your machine and ensure you have a working python environment.
- Ensure you have all required modules:
  - pip3 install requests
- Open main.py and fill the list: PASSWORDS with string values of the passwords you'd like to check
- Run program

## More Information:
The following program was written to give users more security when checking for
  Leaked passwords. It takes in a list of passwords the user would like to check for,
  and creates a utf-8 hash of the password. It then sends the first 5 digites of this
  hash to an API. The said API then returns sets of the hashes that match
  the sent query along with a count of how many times that password has been leaked.
  This program then compares that with the remaining hash that wasn't sent and reports to the
  user the amount of times their password has been leaked.
  
In order to check for leaked passwords, the user must modify the PASSWORDS list.
  It is recommended that the user also delete their passwords from said list after
  the program has finished to ensure optimal security.
