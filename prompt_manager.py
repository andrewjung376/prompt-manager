"""나만의 프롬프트 관리 프로그램 (콘솔 기반)"""

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

DEFAULT_PROMPTS = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝은 스튜디오 조명, 깔끔한 흰색 배경, 제품이 중앙에 크게 보이는 구도, 고해상도.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "광고 스크립트 작성",
        "content": "15초 분량의 제품 광고 영상 스크립트를 작성해주세요. 장면별 화면 묘사, 내레이션, 자막을 표 형식으로 정리해주세요.",
        "category": "영상 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다. 비전문가도 이해할 수 있게 쉬운 비유로 설명하고, 답변 끝에 실행 가능한 다음 단계 3가지를 제시해주세요.",
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": "아래 뉴스 기사를 3줄로 요약하고, 핵심 키워드 5개와 독자가 알아야 할 시사점 1가지를 덧붙여주세요.",
        "category": "자동화",
        "favorite": False,
    },
]

categories = list(CATEGORIES)
prompts = [dict(p) for p in DEFAULT_PROMPTS]

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
