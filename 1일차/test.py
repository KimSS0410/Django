# config > urls.py

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