from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Poll, Option, PollSubmission, SubmissionOption

def index(request):
	polls = Poll.objects.all().order_by('-start_date')
	return render(request, 'poll/index.html', {'polls': polls})

def view_poll(request, id):
	poll = Poll.objects.select_related().get(pk=id)
	return render(request, 'poll/view_poll.html', {'poll': poll})

@login_required(login_url='accounts.login')
def new_poll(request):
	return render(request, 'poll/new_poll.html')

@login_required(login_url='accounts.login')
def save_poll(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		response_type = request.POST.get('response_type')
		creator = request.user
		anonymous_creator = request.POST.get('anonymous_creator')
		start_date = request.POST.get('start_date')
		end_date = request.POST.get('end_date')

		options = request.POST.getlist('options')

		poll = Poll(title=title, response_type=response_type, creator=request.user, anonymous_creator=anonymous_creator, start_date=start_date, end_date=end_date)
		poll.save()

		for op_title in options:
			if len(op_title):
				op = Option(title=op_title, poll=poll)
				op.save()

		return redirect('poll.home')
		#return render(request, 'poll/new_poll.html')

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

def view_result(request, id):
	poll = get_object_or_404(Poll, pk=id)
	return render(request, 'poll/view_result.html', {'poll': poll})
