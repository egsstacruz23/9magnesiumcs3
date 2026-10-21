## Defines the bank account class
class BankAccount:
  def __init__(self, account_number: int, balance):
    self.__account = account_number
    self.__balance = balance

  ## setter and getter methods for account number
  @account.setter
  def set_account_number(self, account_number):
    self.__account = account_number

  @property
  def get_account_number(self):
    return self.__account

  ## setter and getter methods balance
  def set_account_number(self, balance: float = 0.0):
    self.__balance = balnce
    
  def get_balance(self):
    return self.__balance

   
## Prints the output
print("Account number 1")
a1 = BankAccount(12345, 1000)
print("Account number: ", a1.get_account_number)
print("Balance: ", a1.get_balance)
print("")
