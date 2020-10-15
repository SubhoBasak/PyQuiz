from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.utils import timezone
from .models import Score, Question, QuestionSet, Exam
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
    exams = Exam.objects.all()
    scores = []
    for e in exams:
        try:
            scores.append(Score.objects.get(user=request.user, exam=e))
        except Score.DoesNotExist:
            scores.append(-1)
    exam_score_zip = zip(exams, scores)
    return render(request, 'index.html', {'es_zip': exam_score_zip})


@login_required
def quiz_view(request, eid):
    try:
        exam = Exam.objects.get(id=eid)
    except Exam.DoesNotExist:
        return redirect(reverse('index'))
    if 'submit' in request.POST:
        question_set = QuestionSet.objects.filter(user=request.user, exam=exam)
        score = 0
        for q in question_set:
            q.confidence = request.POST['conf_'+str(q.question.id)]
            q.answered = request.POST[str(q.question.id)][0]
            q.save()
            if request.POST[str(q.question.id)][0] == q.question.answer:
                score += 1
        # result = Score(user=request.user, score=score, exam=exam)
        # result.save()
        try:
            result = Score.objects.get(user=request.user, exam=exam)
            result.end = timezone.now()
            result.score = score
            result.save()
        except Score.DoesNotExist:
            return redirect(reverse('index'))
        # for q in question_set:
        #     q.delete()
        return redirect('/score/'+str(exam.id)+'/')

    question_set = QuestionSet.objects.filter(user=request.user, exam=exam)
    if len(question_set) == 0:
        score = Score(user=request.user, exam=exam)
        score.save()
        questions = Question.objects.filter(exam=exam)
        try:
            questions = random.sample(list(questions), exam.questions)
        except Exception as e:
            return redirect(reverse('index'))
        question_set = []
        for qus in questions:
            q = QuestionSet(user=request.user, question=qus, exam=exam, score=score)
            q.save()
            question_set.append(q)
    return render(request, 'quiz.html', {'q': question_set})


@login_required
def score_view(request, eid):
    try:
        exam = Exam.objects.get(id=eid)
        scores = Score.objects.filter(user=request.user)[::-1]
        return render(request, 'score.html',
                      {'total_questions': exam.questions, 'correct': scores[0].score,
                        'incorrect': exam.questions-scores[0].score})
    except Exception as e:
        return redirect(reverse('index'))