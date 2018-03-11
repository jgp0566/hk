from django.shortcuts import render
from django.http import HttpResponse

from .models import Koreans

def index(request):
    #Koreans.get_all_news()
    koreans = Koreans.objects.all()
    context = {'koreans' : koreans} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'transfapp/index.html', context)