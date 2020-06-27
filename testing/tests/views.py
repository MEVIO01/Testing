from django.shortcuts import render
from .models import Test


def tests_view(request):
    available_tests = Test.objects.all()
    context = {'tests': available_tests}
    return render(request, 'tests/tests.html', context)

