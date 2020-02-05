from django.contrib import admin
from . models import Poll, Option, PollSubmission, SubmissionOption

admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(PollSubmission)
admin.site.register(SubmissionOption)