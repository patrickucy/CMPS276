from django.shortcuts import *
from app01.models import *
from django.core import serializers
import json
import datetime


# Create your views here.
def index(request):
    return render_to_response('index.html')


def test(request):
    return render_to_response('test.html')


def get_data(request):
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

    # print '-------', request.GET['timeSpan'], '--------------'

    time_span = request.GET['timeSpan']

    start_month = int(time_span[0:2])
    start_day = int(time_span[3:5])
    start_year = int(time_span[6:11])
    end_month = int(time_span[13:15])
    end_day = int(time_span[16:18])
    end_year = int(time_span[19:24])

    print "##################", start_month, "*", start_day, "*", start_year, ":", end_month, "*", end_day, "*", end_year

    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)

    data_output = [obj.as_json() for obj in
                   FakeOutput.objects.filter(time_stamp__range=(start_date, end_date)).order_by('time_stamp')]

    log_output = [obj.as_json() for obj in FakeLog.objects.filter(time_stamp__range=(start_date, end_date)).order_by('time_stamp')]


    data = {
        'output': data_output,
        'log': log_output
    }
    print '*****', data, '******'
    return HttpResponse(json.dumps(data), content_type="application/json")
