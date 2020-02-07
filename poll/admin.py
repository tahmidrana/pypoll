from django.contrib import admin
from . models import Poll, Option, PollSubmission, SubmissionOption

admin.site.register(Poll)
admin.site.register(Option)

class PollSubmissionAdmin(admin.ModelAdmin):
	list_display = ['poll', 'ip_addr']
admin.site.register(PollSubmission, PollSubmissionAdmin)


class SubmissionOptionAdmin(admin.ModelAdmin):
	list_display = ['submission', 'option']
admin.site.register(SubmissionOption, SubmissionOptionAdmin)