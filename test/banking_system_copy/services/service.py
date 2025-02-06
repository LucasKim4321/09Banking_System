# from models.user import User           # models/user.py에서 User 클래스 임포트
# from utils.exceptions import *      # utils/exceptions.py의 모든 예외 임포트

from ..models.user import User           # models/user.py에서 User 클래스 임포트
from ..utils.exceptions import *      # utils/exceptions.py의 모든 예외 임포트

class BankingService:
    def __init__(self) -> None:
        self.users = list()
    def add_user(self,username: str) -> None:
        self.users.append(User(username))
    def remove_user(self,username: str) -> bool:
        user = self.find_user(username)

        if isinstance(user, User):
            self.users.remove(user)
            return True
        else:
            return False
        
    def find_user(self, username: str) -> User:
        try:
            # for문을 사용해 유저를 찾음
            for user in self.users:
                if username == user.username:
                    return user # 유저를 찾으면 유저 객체를 리턴시키면서 함수 종료.
                
            # for문을 사용해 유저를 찾지 못하면 에러를 발생 시킴
            raise UserNotFoundError(username)
        
        # 에러 처리
        except UserNotFoundError as e:
            print("유저를 찾을 수 없습니다!")
            print(e)
            return False
        except Exception as e:
            print("문제가 발생했습니다!")
            print(e)
            return False
    def user_menu(self, username: str) -> None:
        user = self.find_user(username)
        # User 클래스로 생성된 user 인스턴스 인지 판별
        if isinstance(user, User):
            while True:
                choice = input("원하는 서비스 코드를 입력해주세요. 1.입금 2.출금 3.잔고확인 4.거래내역 0.종료").strip()

                # 서비스 코드를 입력하지 않으면 다시
                if not choice.isdigit():
                    input("서비스 코드를 입력해주세요!")
                    continue            
                
                # 서비스 종료
                if choice == '0':
                    input("서비스를 종료합니다 :b")
                    print("-----------------------------------------------------")
                    break

                # 입금 서비스
                if choice == '1':
                    while True:
                        amount = input("입금할 금액을 입력해주세요~").strip()

                        # 숫자 입력시
                        if amount.isdigit():
                            amount = int(amount)

                        # 숫자 미 입력시 다시
                        else:
                            input("서비스 코드를 입력해주세요!")
                            continue
                        
                        # user.account의 deposit 메소드 실행
                        user.account.deposit(amount)

                        print("-----------------------------------------------------")

                        # 입금 서비스 종료
                        break

                    # 처음 서비스 입력 화면으로 돌아감
                    continue

                # 출금 서비스
                if choice == '2':
                    while True:
                        amount = input("출금할 금액을 입력해주세요~").strip()

                        # 숫자 입력시
                        if amount.isdigit():
                            amount = int(amount)

                        # 숫자 미 입력시 다시
                        else:
                            input("서비스 코드를 입력해주세요!")
                            continue
                        
                        # user.account의 withdraw 메소드 실행
                        user.account.withdraw(amount)

                        print("-----------------------------------------------------")

                        # 출금 서비스 종료
                        break

                    # 처음 서비스 입력 화면으로 돌아감
                    continue

                # 잔고확인
                if choice == '3':
                    input("잔고를 확인하겠습니다.")
                                        
                    # user.account의 withdraw 메소드 실행
                    print(f"계좌 잔고는 {user.account.get_balance()}원 입니다.")

                    print("-----------------------------------------------------")

                    # 처음 서비스 입력 화면으로 돌아감
                    continue

                # 거래내역
                if choice == '4':
                    input("거래내역을 확인하겠습니다.")
                        
                    # user.account의 withdraw 메소드 실행
                    for i in user.account.get_transactions():
                        print(f"{i[0]} : {i[1]}원 계좌잔고: {i[2]}원")

                    print("-----------------------------------------------------")

                    # 처음 서비스 입력 화면으로 돌아감
                    continue
