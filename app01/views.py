from django.shortcuts import *
from app01.models import *
from django.core import serializers
import json


# Create your views here.
def index(request):
    return render_to_response('index.html')


def test(request):
    return render_to_response('test.html')


def getData(request):
    data = [
        {
            'username': 'patrick',
            'password': '1234',
            'last_name': 'yu',
            'first_name': 'cy',
            'age': '23'
        }, {
            'username': 'tom',
            'password': '465',
            'last_name': 'jack',
            'first_name': 'harry',
            'age': '18'
        }, {
            'username': 'sally',
            'password': '0987',
            'last_name': 'zhang',
            'first_name': 'lili',
            'age': '29'
        }, {
            'username': 'hello',
            'password': '77766',
            'last_name': 'lin',
            'first_name': 'ppp',
            'age': '18'
        }
    ]

    data = [obj.as_json() for obj in FakeData.objects.all()]
    return HttpResponse(json.dumps(data), content_type="application/json")
