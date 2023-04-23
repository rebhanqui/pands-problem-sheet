# program that reads in 10 digits and outputs same digits with only last 4 showing and first 6 replaced with X's
# Author: Rebecca Quinn

# takes in the users account number
account_raw = input("Please enter your account number: ")

#hides all digits except the last four no matter the account number length
account_safe = "".join(['#' for x in account_raw[:-4]]) + account_raw[-4:]

# confirms last 4 digits of account hiding the first 6 digits via index and prints the result
account_secure = (f"Account number: {account_safe}")
print(account_secure)