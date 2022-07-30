import django.contrib.auth.views

#import django.contrib.sessions as sessions
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.contrib import messages
#from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from qa.models import Question, Answer, Session
from qa.forms import AskForm, AnswerForm, SignupForm
from qa.misc import do_login, generate_long_random_key, get_username_from_request
#import models


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return (paginator, page)


def base_view(request, funct, title, baseurl):
    questions = funct
    (paginator, page) = paginate(request, questions)
    return render(request, 'questions_list.html', {
        'title': title,
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        'page_numbers_list': range(1, paginator.num_pages + 1),
        'baseurl': baseurl,
        'user': get_username_from_request(request),
        #'sessionid': request.COOKIES.get('sessionid')
    })


@require_GET
def popular_view(request):
    return base_view(request, Question.objects.popular(), 'Популярные вопросы', '/popular/?page=')


@require_GET
def new_view(request):
    return base_view(request, Question.objects.new(), 'Новые вопросы', '/?page=')


def question_view(request, id):
    question = get_object_or_404(Question, id=id)
    try:
        answers = Answer.objects.filter(question=question)
    except Answer.DoesNotExist:
        answers = None
    if request.method == "POST":
        form = AnswerForm(data=request.POST, question_id=id)
        form._user = get_username_from_request(request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/question/' + str(id))
        #else:
        #    messages.error(request, "Error")
    else:
        form = AnswerForm()
    return render(request, 'question_details.html', {
            'question': question,
            'answers': answers,
            'form': form
    })


def question_add(request):
    if request.method == "POST":
        form = AskForm(data=request.POST)
        form._user = get_username_from_request(request)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect('/question/' + str(question.id))
    else:
        form = AskForm()
    return render(request, 'question_add.html', {
            'form': form
    })


def signup_view(request):
    error = ''
    if request.method == "POST":
        #url = request.POST.get('continue', '/')  # Так правильно
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = '/'  # Для прохождения теста
        form = SignupForm(data=request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
            except User.DoesNotExist:  #
                user = form.save()  # TODO: обработать ошибку существования такого пользователя в БД
                sessionid = do_login(username, password)  # TODO: попробовать реализовать средствами django.contrib.auth.login
                response = HttpResponseRedirect(url)
                response.set_cookie('sessionid', sessionid,
                                    domain='localhost', httponly=True,
                                    expires=datetime.now() + timedelta(days=1))
                return response
                #login(request, user)
            error = 'Такой юзер уже экзист!'
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form,
        'error': error
    })


def login_view(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #url = request.POST.get('continue', '/')  # Так правильно
        url = '/'  # Для прохождения теста
        sessionid = do_login(username, password)  # TODO: попробовать реализовать средствами django.contrib.auth.login
        if sessionid:
            response = HttpResponseRedirect(url)
            response.set_cookie('sessionid', sessionid,
                            domain='localhost', httponly=True,
                            expires=datetime.now() + timedelta(days=1))
            return response
        else:
            error = u'Wrong login / password'
            form = AuthenticationForm()
            #return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {
        'form': form,
        'error': error  # TODO: error никак не используется
    })