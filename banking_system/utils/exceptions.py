class InsufficientFundsError(Exception):
    """잔액이 부족할 때 발생하는 예외"""
    def __init__(self, message="Insufficient funds for the transaction."):
        super().__init__(message)

class NegativeAmountError(Exception):
    """금액이 0 이하일 때 발생하는 예외"""
    def __init__(self, message="Transaction amount must be greater than 0."):
        super().__init__(message)

class UserNotFoundError(Exception):
    """사용자를 찾을 수 없을 때 발생하는 예외"""
    def __init__(self, username):
        super().__init__(f"User '{username}' not found.")
        self.username = username