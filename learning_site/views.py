__author__ = 'om'

from django.http import HttpResponse


def test(request):
    return HttpResponse('Hello World')
