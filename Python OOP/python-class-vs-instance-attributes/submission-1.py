class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    def __init__(self, name:str, balance:int) -> None:
        self.__name = name
        self.__balance = balance
        BankAccount.total_accounts+=1
        BankAccount.total_balance+=balance

    def account_infos(self) -> str:
        print(f"{self.__name}'s balance: ${self.__balance}")

# TODO: Create two accounts
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
alice_account.account_infos()
bob_account.account_infos()

print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")