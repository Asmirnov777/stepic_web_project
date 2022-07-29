from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.contrib import messages
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
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
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect('/question/' + str(question.id))
    else:
        form = AskForm()
    return render(request, 'question_add.html', {
            'form': form
    })
