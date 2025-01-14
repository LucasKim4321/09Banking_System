# from .transaction import transaction
# import transaction
from .transaction import Transaction

class Account:
    bank_name = ''

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name
        
    def __init__(self) -> None:
        self.transactions = list()
        self.__balance = 0
    def deposit(self, amount: int) -> None:
        if amount > 0:
            
            self.__balance += amount
            
            # Transaction 클래스를 사용해 거래내역 제어
            transaction = Transaction('입금', amount, self.__balance)
            self.transactions.append(transaction.to_tuple())
            print(str(transaction))
    def withdraw(self, amount: int) -> None:
        if amount > 0:
            if amount > self.__balance:
                amount = self.__balance
                
            self.__balance -= amount

            # Transaction 클래스를 사용해 거래내역 제어
            transaction = Transaction('출금', amount, self.__balance)
            self.transactions.append(transaction.to_tuple())
            print(str(transaction))
    def get_balance(self) -> int:
        return self.__balance
    def get_transactions(self) -> list: 
        return self.transactions