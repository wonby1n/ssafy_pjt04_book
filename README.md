📚 04_pjt - 도서 데이터 관리 웹 애플리케이션
1. 프로젝트 개요

이 프로젝트는 Django 웹 프레임워크와 Bootstrap을 활용하여 도서 데이터를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)할 수 있는 웹 애플리케이션입니다.
추가적으로 생성형 AI를 활용하여 작가 정보 자동 생성 기능을 확장할 수 있도록 설계되었습니다

04-pjt-명세서

.

2. 개발 환경

언어 및 툴

Python 3.11

Django 5.2

HTML, CSS

Bootstrap 5.3

VS Code, Google Chrome

데이터베이스

SQLite3 (Django 기본 DB)

3. 주요 기능 (CRUD)
✅ 필수 기능

Index (전체 도서 조회)

전체 도서 목록을 카드(Grid) 형식으로 조회 가능

각 도서에 대해 Detail 버튼을 통해 상세 페이지 이동

Create (도서 등록)

new 페이지에서 도서 제목, 설명, 리뷰 평점, 저자 입력

저장 후 detail 페이지로 리다이렉트

Detail (도서 상세 페이지)

선택한 도서의 상세 정보 출력

Update, Delete, Back 버튼 제공

Update (도서 수정)

수정 페이지에서 기존 값이 채워진 Form 제공

수정 후 다시 detail 페이지로 리다이렉트

Delete (도서 삭제)

detail 페이지에서 Delete 버튼 클릭 시 삭제

삭제 후 index 페이지로 리다이렉트

4. 프로젝트 구조
mypjt/
 ├── books/                 # 앱
 │   ├── migrations/
 │   ├── templates/books/   # HTML 템플릿
 │   │   ├── base.html
 │   │   ├── index.html
 │   │   ├── detail.html
 │   │   ├── new.html
 │   │   └── edit.html
 │   ├── models.py          # Book 모델
 │   ├── views.py           # CRUD 뷰 함수
 │   └── urls.py            # 앱 라우팅
 ├── mypjt/                 # 프로젝트 설정
 │   ├── settings.py
 │   ├── urls.py
 └── db.sqlite3

5. Book 모델
class Book(models.Model):
    title = models.CharField(max_length=100)      # 도서 제목
    description = models.TextField()              # 도서 설명
    review_num = models.IntegerField()            # 회원 리뷰 평점
    author = models.CharField(max_length=50)      # 저자 이름

6. UI/UX

Bootstrap Navbar: index, new 페이지 이동 편리성 제공

Bootstrap Grid/Card: 도서 목록을 카드 형식으로 3~4개씩 정렬

버튼 스타일링: CRUD 기능을 직관적으로 수행할 수 있도록 디자인

7. 도전 과제 (선택)

생성형 AI + 위키피디아 API 연동

저자 이름으로 위키피디아에서 정보 검색

GPT API 활용 → 작가 소개, 대표작, 프로필 이미지 자동 생성

Book 모델에 필드 추가:

author_img_url, author_info, author_works

상세 페이지 하단에 작가 정보 영역 표시

8. 실행 방법
# 가상환경 실행
python -m venv venv
source venv/Scripts/activate   # (Windows)
source venv/bin/activate       # (Mac/Linux)

# Django 설치
pip install django==5.2

# 서버 실행
python manage.py runserver


브라우저에서 http://127.0.0.1:8000/books/ 접속

9. 학습 내용 & 느낀 점

Django의 Model-View-Template(MVT) 구조 이해

ORM을 활용한 DB 조작 경험

Bootstrap을 통한 빠른 UI 구성

CRUD 흐름을 직접 구현하면서 웹 앱 제작의 전반적인 구조 학습

(도전) AI API 활용 시, 단순 CRUD를 넘어 확장 가능한 서비스 설계 가능성 체감