from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'poll/home.html', context)

def create(request):
    context = {}
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    context = {}
    return render(request, 'poll/poll.html', context)

def results(request, poll_id):
    context = {}
    return render(request, 'poll/results.html', context)