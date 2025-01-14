from typing import Callable
from .exceptions import NegativeAmountError

def validate_transaction(func: Callable) -> Callable:
    """
    데코레이터: 금액이 0보다 큰지 확인합니다.
    금액이 0 이하일 경우 NegativeAmountError를 발생시킵니다.
    """
    def wrapper(*args, **kwargs):
        # 첫 번째 매개변수 또는 키워드 매개변수로 amount 확인
        amount = kwargs.get('amount') if 'amount' in kwargs else args[0]
        
        if amount <= 0:
            raise NegativeAmountError(f"Invalid transaction amount: {amount}. Must be greater than 0.")
        
        return func(*args, **kwargs)
    
    return wrapper
