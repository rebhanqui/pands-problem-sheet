# program that reads in 10 digits and outputs same digits with only last 4 showing and first 6 replaced with X's
# Author: Rebecca Quinn

# takes in the users account number
account_raw = input("Please enter your 10 digit account number: ")

# confirms last 4 digits of account hiding the first 6 digits via index and prints the result
account_secure = (f"Account number: XXXXXX{account_raw[-4:]}")
print(account_secure)