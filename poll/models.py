from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
	SINGLE_RESPONSE = 1
	MULTIPLE_RESPONSE = 2

	RESPONSE_CHOICES = [
		(SINGLE_RESPONSE, 'Single Response'),
		(MULTIPLE_RESPONSE, 'Multiple Response'),
	]

	title = models.CharField(max_length=200)
	descr = models.TextField(null=True, blank=True)
	response_type = models.SmallIntegerField(choices=RESPONSE_CHOICES, default=SINGLE_RESPONSE)
	creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	anonymous_creator = models.BooleanField(default=False)
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.title


class Option(models.Model):
	title = models.CharField(max_length=100)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def submission_counts(self):
		return self.submissionoption_set.count()

	def submission_percentage(self):
		total_submitted_option_count = self.poll.pollsubmission_set.count()
		this_option_submission_count = self.submissionoption_set.count()
		this_option_submission_percentage = 0
		if total_submitted_option_count > 0:
			this_option_submission_percentage = (this_option_submission_count * 100) / total_submitted_option_count
		return int(this_option_submission_percentage)


class PollSubmission(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	ip_addr = models.CharField(max_length=40)

	#class Meta:
		#unique_together = ['poll', 'ip_addr']

	def __str__(self):
		return self.poll.title

class SubmissionOption(models.Model):
	submission = models.ForeignKey(PollSubmission, on_delete=models.CASCADE)
	option = models.ForeignKey(Option, on_delete=models.CASCADE)

	def __str__(self):
		return self.submission.poll.title
