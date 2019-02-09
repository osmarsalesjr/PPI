from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html',
                  {'questions': questions})


def show_question(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question_id)
    return render(request, 'question.html',
                  {'question': question,
                   'choices': choices})


def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question_id)
    return render(request, 'vote.html',
                  {'question': question,
                   'choices': choices})


def vote_choice(request, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('index')


def show_results(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question_id)
    sum_votes = sum([choice.votes for choice in choices])
    if sum_votes > 0:
        results = [{'choice': choice, 'result': round(((choice.votes / float(sum_votes)) * 100.0), 2)} for choice in choices]
    else:
        results = [{'choice': choice, 'result': 0.0} for choice in choices]
    return render(request, 'results.html', {'question': question,
                                            'choices': choices,
                                            'results': results})


def manage_question(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question_id)
    return render(request, 'manage_question.html',
                  {'question': question,
                   'choices': choices})


def remove_choice(request, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.delete()

    return redirect('index')


def close_question(request, question_id):
    question = Question.objects.get(id=question_id)
    question.closed = True
    question.save()

    return redirect('index')


def open_question(request, question_id):
    question = Question.objects.get(id=question_id)
    question.closed = False
    question.save()

    return redirect('index')
