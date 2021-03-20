from django.shortcuts import render
from .models import Adviser
from .serializers import AdviserSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def adviser_api(request):
    if(request.method == 'GET'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            adv = Adviser.objects.get(id=id)
            serialize = AdviserSerializer(adv)
            json_data = JsonRenderer().render(serialize.data)
            return HttpResponse(json_data, content_type = 'application/json')
@csrf_exempt
def adviser_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = AdviserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResposnse(json_data,content_type = 'application/json')
        return HttpResponse(JSONRenderer().render(serializer.error),content_type= 'application/json')