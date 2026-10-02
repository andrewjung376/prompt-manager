"""나만의 프롬프트 관리 프로그램 (콘솔 기반)"""


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    try:
        while True:
            show_menu()
            choice = input("선택: ").strip()
            if choice == "0":
                print("프로그램을 종료합니다.")
                break
            else:
                print("올바른 번호를 입력하세요.")
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
