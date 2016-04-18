from django.shortcuts import *


# Create your views here.
def index(request):
    return render_to_response('index.html')


def test(request):
    return render_to_response('test.html')
