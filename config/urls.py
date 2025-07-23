"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#영화 페이지 만들기
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404


def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404

    movie = movie_list[index]

    context = {'movie': movie}
    return render(request, 'movie.html', context)

#도서 페이지 만들기
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404


def book_list(request):
    book_text = ''

    return render(request, 'book_list.html', {'range': range(0, 10)})


def book(request, num):
    return render(request, template_name='book_detail.html', context={'num': num})



#구구단
def gugu(request, num):
    context = {
        'num': num,
        'results': [num * i for i in range(1, 10)]
    }
    return render(request, 'gugu.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gugu/<int:num>/', gugu),
]











from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 간단한 HTTP 응답 만들어보기
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # HttpResponse 모듈 import


def index(request):
    return HttpResponse('<h1>hello</h1>')


def book_list(request):
    book_text = ''

    for i in range(0, 10):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)


def book(request, num):
    book_text = f'book {num}번 페이지입니다'
    return HttpResponse(book_text)


def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.')


urlpatterns = [
    path('admin/', admin.site.urls),  # 기본적으로 Django에서 제공하는 관리자페이지 url
    path('', index),
    path('book_list', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),
]

# 가짜 DB를 추가하고 활용해보기
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404

# 가짜 DB
movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '웡카', 'director': '폴 킹'},
    {'title': '듄: 파트 2', 'director': '드니 빌뇌브'},
    {'title': '시민덕희', 'director': '박영주'},

]


def movies(request):
    movie_titles = [movie['title'] for movie in movie_list]

    response_text = '<br>'.join(movie_titles)
    return HttpResponse(response_text)


def movie_detail(request, index):
    # 예외처리
    # movie_list의 데이터 개수보다 큰 index 입력 시
    # 404 Error를 보여줍니다.

    if index > len(movie_list) - 1:
        raise Http404

    movie = movie_list[index]

    response_text = f'<h1>{movie["title"]}</h1> <p>감독: {movie["director"]}</p>'
    return HttpResponse(response_text)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
]


#영화 제목을 클릭하면 해당 영화의 상세페이지로 이동하는 기능 구현
def movies(request):
    movie_titles = [movie['title'] for movie in movie_list]

    response_text = ''

    for index, title in enumerate(movie_titles):
        response_text += f'<a href="/movie/{index}/">{title}</a><br>'
    return HttpResponse(response_text)


def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404
    movie = movie_list[index]

    response_text = f'<h1>{movie["title"]}</h1> <p>감독: {movie["director"]}</p>'
    return HttpResponse(response_text)


# movie 함수 같은 결과를 보여주는 다른 코드
def movies(request):
    movie_titles = [
        f'<a href="/movie/{index}/">{movie['title']}</a>'
        for index, movie in enumerate(movie_list)
    ]

    response_text = '<br>'.join(movie_titles)

    return HttpResponse(response_text)