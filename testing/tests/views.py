from django.shortcuts import render
from .models import Test, Question


def tests_view(request):
    available_tests = Test.objects.all()
    context = {'tests': available_tests}
    return render(request, 'tests/tests.html', context)


def questions_view(request, id=None):
    questions = Question.objects.filter(tests__id=id)
    context = {'questions': questions}
    return render(request, 'tests/questions.html', context)

