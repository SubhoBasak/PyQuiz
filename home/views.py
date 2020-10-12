from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from .models import Score


def login_view(request):
    if 'login' in request.POST:
        pass
    return render(request, 'login.html', {})


@login_required
def index_view(request):
    if 'submit' in request.POST:
        result = Score(user=User, score=request.POST['score'])
    return render(request, 'index.html')


def score_view(request):
    return render(request, 'score.html')