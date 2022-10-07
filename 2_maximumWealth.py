# m*n inte
import random

MINIMUM_N_ACCOUNTS = 1
MINIMUM_N_CUSTOMERS = 2
MAX_N_CUSTOMERS = 50
MAX_N_ACCOUNTS = 10
MAX_AMOUNT_MONEY = 100
MIN_AMOUNT_MONEY = 0

def random_customer_number():
  return random.randint(MINIMUM_N_CUSTOMERS, MAX_N_CUSTOMERS)

def random_account_number():
  return random.randint(MINIMUM_N_ACCOUNTS, MAX_N_ACCOUNTS)

def random_amount_money(max_money):
  return random.randint(MIN_AMOUNT_MONEY, max_money)

def inital_random_input(n_customers=None, n_accounts=None, max_money=None, random=True):
  accounts = []
  customer_number = n_customers if not random else random_customer_number()
  account_number = n_accounts if not random else random_account_number()
  
  for i in range(customer_number):
    user_accounts = []
    for j in range(account_number): 
      user_accounts.append(random_amount_money(max_money))
    accounts.append(user_accounts)
  return accounts

def calculate(accounts):
  max = 0
  account_index = 0
  for index in range(len(accounts)):
    account = accounts[index]
    if sum(account) > max:
      max = sum(account)
      account_index = index
  return {"Wealth": max, "Account": accounts[account_index]}

if __name__=="__main__":
  accounts = inital_random_input(3, 3, 10, random = False)
  account_info = calculate(accounts)
  print("The richest customer has {account}, Wealth is {wealth}".format(account=account_info["Account"], wealth=account_info["Wealth"]))