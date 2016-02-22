from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Question, Answer

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('feedback/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'feedback/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'feedback/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'feedback/results.html', {'question': question})

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_answer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'feedback/detail.html', {
            'question': question,
            'error_message': "You didn't select an answer.",
        })
    else:
        selected_answer.votes += 1
        selected_answer.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('feedback:results', args=(question.id,)))