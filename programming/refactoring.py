from review_manager import ReviewManager

manager = ReviewManager()
manager.add_review("파이썬 기초", 5)
manager.add_review("파이썬 기초", 4)
manager.add_review("딥러닝 입문", 5)
manager.add_review("딥러닝 입문", 1)
manager.add_review("웹 개발 입문", 4)
manager.add_review("딥러닝 입문", 1)

print(f"파이썬 기초 평균: {manager.get_average('파이썬 기초'):.2f}")  # 4.5
print(f"딥러닝 입문 평균: {manager.get_average('딥러닝 입문'):.2f}")  # 4.0

top_title, top_score = manager.get_top_book()
print(f"최고 평점 도서: {top_title} ({top_score:.1f})")