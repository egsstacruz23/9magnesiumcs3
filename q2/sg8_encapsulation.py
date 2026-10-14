## Defines the bank account class
class BankAccount:
  def __init__(self, account_number, balance):
    self.__account = account_number
    self.__balance = balance

  def get_account_number(self):
    return self.__account

   
## Prints the output
a1 = BankAccount(12345, 1000)
print("Account number: ", a1.get_account_number())
