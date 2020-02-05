from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Poll, PollSubmission, SubmissionOption

def index(request):
	polls = Poll.objects.all()
	return render(request, 'poll/index.html', {'polls': polls})

def view_poll(request, id):
	poll = Poll.objects.select_related().get(pk=id)
	return render(request, 'poll/view_poll.html', {'poll': poll})

@login_required(login_url='accounts.login')
def new_poll(request):
	return render(request, 'poll/new_poll.html')

def submit_response(request, id):
	if request.method == 'POST':
		options = request.POST.get('options')
		#ip_addr = 
		data = {
			'status': 1,
			'message': 'Saved Successfully'
		}
		return JsonResponse(data)
	else:
		return HttpResponse(Poll.objects.get(pk=id))