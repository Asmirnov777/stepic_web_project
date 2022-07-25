from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
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


@require_GET
def question_view(request, id):
#    try:
#        question = Question.objects.get(id=id)
#    except Question.DoesNotExist:
#        raise Http404
    question = get_object_or_404(Question, id=id)
    try:
        answers = Answer.objects.filter(question_id=question.id)
    except Answer.DoesNotExist:
        answers = None
    return render(request, 'question_details.html', {
            'question': question,
            'answers': answers
    })


@require_GET
def popular_view(request):
    questions = Question.objects.popular()
    (paginator, page) = paginate(request, questions)
    return render(request, 'questions_list.html', {
            'title': 'Популярные вопросы',
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
            'page_numbers_list': range(1, paginator.num_pages + 1),
            'baseurl': '/popular/?page=',  # TODO: сделать через reverse
    })


@require_GET
def new_view(request):
    questions = Question.objects.new()
    (paginator, page) = paginate(request, questions)
    return render(request, 'questions_list.html', {
            'title': 'Новые вопросы',
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
            'page_numbers_list': range(1, paginator.num_pages + 1),
            'baseurl': '/?page=',  # TODO: сделать через reverse
    })