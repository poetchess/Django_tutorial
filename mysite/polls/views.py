from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    # use the shortcut provided by Django.ß
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})
    '''

    # common to use get() and raise Http404 if the object doesn't exist.
    # use another shortcut provided by Django
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    reponse = "You're looking at the results of question {}"
    return HttpResponse(reponse.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))
