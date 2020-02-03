from django.shortcuts import render
from django.http import HttpResponse
from . models import Poll

def index(request):
	polls = Poll.objects.all()
	return render(request, 'poll/index.html', {'polls': polls})

def view_poll(request, id):
	poll = Poll.objects.select_related().get(pk=id)
	return render(request, 'poll/view_poll.html', {'poll': poll})

def new_poll(request):
	return render(request, 'poll/new_poll.html')