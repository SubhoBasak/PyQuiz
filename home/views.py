from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from .models import Score, Question
import itertools as it
import random
import string


def login_view(request):
    status = 0
    if 'email' in request.POST and 'password' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect(reverse('index'))
            else:
                status = 1
        except User.DoesNotExist:
            status = 2
    return render(request, 'login.html', {'status': status})


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


def forgot_view(request):
    status = 0
    if 'email' in request.POST:
        try:
            user = User.objects.get(email=request.POST['email'])
            send_mail('Reset password',
                      'Reset your password here: https://subhobasak.pythonanywhere.com/reset/'+str(user.id)+'/',
                      'subhobasak22@gmail.com', [user.email,])
        except User.DoesNotExist:
            status = 1
    return render(request, 'forgot.html', {'status': status})


def reset_view(request, uid):
    status = 0
    if 'new_pswd' in request.POST and 'cnfrm_pswd' in request.POST:
        if request.POST['new_pswd'] == request.POST['cnfrm_pswd']:
            try:
                user = User.objects.get(id=uid)
                user.set_password(request.POST['new_pswd'])
                user.save()
                login(request, user)
                return redirect(reverse('index'))
            except User.DoesNotExist:
                status = 1
        else:
            status = 2
    return render(request, 'reset.html', {'status': status})


def register_view(request):
    if 'first_name' in request.POST and 'last_name' in request.POST \
            and 'email' in request.POST and 'password' in request.POST:
        user = User(first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    username=request.POST['email'])
        user.set_password(request.POST['password'])
        user.save()
        login(request, user)
        return redirect(reverse('index'))
    return render(request, 'register.html')


@login_required
def index_view(request):
    if 'submit' in request.POST:
        result = Score(user=User, score=1)
        result.save()
        return redirect(reverse('score'))
    question = it.combinations_with_replacement(string.ascii_letters, 3)
    question = list(question)
    ques_model = Question(user=request.user)
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q1w1 = ques[0]
    ques_model.q1w2 = ques[1]
    ques_model.q1w3 = ques[2]
    ques_model.q1w4 = ques[3]
    ques_model.q1w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q2w1 = ques[0]
    ques_model.q2w2 = ques[1]
    ques_model.q2w3 = ques[2]
    ques_model.q2w4 = ques[3]
    ques_model.q2w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q3w1 = ques[0]
    ques_model.q3w2 = ques[1]
    ques_model.q3w3 = ques[2]
    ques_model.q3w4 = ques[3]
    ques_model.q3w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q4w1 = ques[0]
    ques_model.q4w2 = ques[1]
    ques_model.q4w3 = ques[2]
    ques_model.q4w4 = ques[3]
    ques_model.q4w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q5w1 = ques[0]
    ques_model.q5w2 = ques[1]
    ques_model.q5w3 = ques[2]
    ques_model.q5w4 = ques[3]
    ques_model.q5w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q6w1 = ques[0]
    ques_model.q6w2 = ques[1]
    ques_model.q6w3 = ques[2]
    ques_model.q6w4 = ques[3]
    ques_model.q6w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q7w1 = ques[0]
    ques_model.q7w2 = ques[1]
    ques_model.q7w3 = ques[2]
    ques_model.q7w4 = ques[3]
    ques_model.q7w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q8w1 = ques[0]
    ques_model.q8w2 = ques[1]
    ques_model.q8w3 = ques[2]
    ques_model.q8w4 = ques[3]
    ques_model.q8w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q9w1 = ques[0]
    ques_model.q9w2 = ques[1]
    ques_model.q9w3 = ques[2]
    ques_model.q9w4 = ques[3]
    ques_model.q9w5 = ques[4]
    ques = random.sample(question, 5)
    ques = [''.join(i) for i in ques]
    ques_model.q10w1 = ques[0]
    ques_model.q10w2 = ques[1]
    ques_model.q10w3 = ques[2]
    ques_model.q10w4 = ques[3]
    ques_model.q10w5 = ques[4]
    ques_model.save()
    return render(request, 'index.html', {'q': ques_model})


@login_required
def score_view(request):
    return render(request, 'score.html')