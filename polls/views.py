from django.shortcuts import get_object_or_404, render, redirect

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
        'choices': question.choices.all(),
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
        'choices': question.choices.all(),
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        user_choice = request.POST['choice']
        choice = Choice.objects.get(id=user_choice)
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'choices': question.choices.all(),
            'error_message': "Tu n'as pas sélectionné de choix.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        choice.votes += 1
        choice.save()
    return redirect('polls:results', question.id)
