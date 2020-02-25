from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
    	username = request.POST.get('username')
    	password = request.POST.get('password')
    	user = authenticate(username=username, password=password)

    	if user is None:
    		return redirect('accounts.login')
    	login(request, user)
    	return redirect('poll.home')


def signup_view(request):
    return render(request, 'accounts/signup.html')


@login_required
def logout_view(request):
	logout(request)
	return redirect('poll.home')

@login_required(login_url='accounts.login')
def profile(request):
    user = request.user
    polls = user.poll_set.all().order_by('-start_date')
    context = {
        'polls': polls
    }
    return render(request, 'accounts/profile.html', context)
