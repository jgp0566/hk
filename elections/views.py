from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate #models에 정의된 Candidate를 import 

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates' : candidates}
    return render(request, 'elections/index.html', context)
