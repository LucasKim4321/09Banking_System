from banking_system.models import User
from banking_system.services import BankingService

def main() -> None:
    banking_service = BankingService()

    while True:
        service_num = input("원하는 서비스 코드를 입력해주세요. 1.사용자 목록 2.사용자 찾기 3.ATM Service 4.사용자 등록 5.사용자 삭제 0.종료").strip()

        # 서비스 코드를 입력하지 않으면 다시
        if not service_num.isdigit():
            input("서비스 코드를 입력해주세요!")
            continue            
        
        # 서비스 종료
        if service_num == '0':
            input("서비스를 종료합니다 :b")
            break
        
        # 사용자 목록
        if service_num == '1':
            for user in banking_service.users:
                print(user)

            print("-----------------------------------------------------")

        # 사용자 찾기
        if service_num == '2':
            while True:
                username = input("찾으실 사용자 이름을 입력해주세요!  0.종료").strip()

                # 종료
                if username == '0':
                    break
                
                # 빈값 입력시 다시
                if username in {''}: # 빈값 입력시.  strip() 사용시 이것만 해도 됨.
                    continue
                
                user = banking_service.find_user(username)
                
                if isinstance(user, User):
                    print(f"사용자: {user.username}를 찾았습니다.")
                    print(user)

                print("-----------------------------------------------------")

                # 종료할 때까지 반복
                continue

            # 처음 서비스 입력 화면으로 돌아감
            continue

        # ATM  Service
        if service_num == '3':
            print("ATM Service를 시작합니다.")

            while True:
                username = input("사용자 이름을 입력해주세요!  0.종료").strip()

                # 종료
                if username == '0':
                    break
                
                # 빈값 입력시 다시
                if username in {''}: # 빈값 입력시.  strip() 사용시 이것만 해도 됨.
                    continue

                # 사용자 메뉴 실행
                banking_service.user_menu(username)

                print("-----------------------------------------------------")

                # 메뉴 종료시 종료
                break
            
            # 처음 서비스 입력 화면으로 돌아감
            continue

        # 사용자 추가
        if service_num == '4':

            while True:
                username = input("추가할 사용자 이름을 입력해주세요!  0.종료").strip()

                # 종료
                if username == '0':
                    break
                
                # 빈값 입력시 다시
                if username in {''}: # 빈값 입력시.  strip() 사용시 이것만 해도 됨.
                    continue

                # 사용자 추가
                banking_service.add_user(username)

                print(f"{username}님을 등록하였습니다.")

                print("-----------------------------------------------------")
                    
                # 메뉴 종료시 종료
                break
            
            # 처음 서비스 입력 화면으로 돌아감
            continue

        # 사용자 삭제
        if service_num == '5':

            while True:
                username = input("삭제할 사용자 이름을 입력해주세요!  0.종료").strip()

                # 종료
                if username == '0':
                    break
                
                # 빈값 입력시 다시
                if username in {''}: # 빈값 입력시.  strip() 사용시 이것만 해도 됨.
                    continue

                # 사용자 삭제
                remove = banking_service.remove_user(username)

                if remove:
                    print("정상적으로 삭제하였습니다.")
                else:
                    print("사용자가 존재하지 않습니다.")
                    continue

                print("-----------------------------------------------------")

                # 메뉴 종료시 종료
                break
            
            # 처음 서비스 입력 화면으로 돌아감
            continue

if __name__ == "__main__":
    main()