# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import Http404

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'core/index.html', context) #'core/index.html' - 'APP_DIRS': True


def hello(request):
    return HttpResponse('Hello world')



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'core/detail.html', {'question': question}) #'core/detail.html - 'APP_DIRS': True'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'core/results.html', {'question': question}) #'core/results.html - 'APP_DIRS': True


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'core/detail.html', {
            'question': p,
            'error_message': "Вы не сделали выбор.",
        }) #'core/detail.html' - 'APP_DIRS': True
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('core:results', args=(p.id,)))
