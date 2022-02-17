from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from cgitb import text
from unicodedata import name
from . models import (Account, 
                    Student,)



def index(request: WSGIRequest) -> HttpResponse:
    """Search the first User"""
    user: User = User.objects.first()
    name: str = user.first_name

    account: Account = user.account
    full_name: str = account.full_name

    student: Student = Student.objects.first()
    student_gpa: float = student.GPA

    text: str = f'<h1>Name: {full_name} \
                    <br> Account {name} \
                    <br> GPA: {student_gpa}'

    response: HttpResponse = HttpResponse(text)
    return response

def index_2 (request: WSGIRequest) -> HttpResponse:
        return HttpResponse(
            '<h1> Страница: Стартовая</h1>'
        )