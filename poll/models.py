from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
	title = models.CharField(max_length=200)
	descr = models.TextField(null=True, blank=True)
	creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.title


class Option(models.Model):
	title = models.CharField(max_length=100)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

	def __str__(self):
		return self.title