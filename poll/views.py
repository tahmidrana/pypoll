from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Poll, Option, PollSubmission, SubmissionOption

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
		options = request.POST.getlist('options')

		if len(options) == 0:
			messages.error(request, 'You have to select atleast one option to submit')
			return redirect('view_poll', id)

		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[-1].strip()
		else:
			ip = request.META.get('REMOTE_ADDR')

		try:
			poll_submission = PollSubmission(poll = Poll.objects.get(pk=id), ip_addr=ip)
			poll_submission.save()
			
			for op in options:
				so = SubmissionOption(submission = poll_submission, option = get_object_or_404(Option, pk=op))
				so.save()
			messages.success(request, 'Thank you, Your response saved successfully.')
			
		except Exception as e:
			messages.error(request, 'Sorry, your response save failed.')
		return redirect('view_poll', id)
	else:
		messages.error(request, 'Bad Request')
		return redirect('view_poll', id)