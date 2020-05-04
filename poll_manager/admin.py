from django.contrib import admin
from .models import PollModel, Comment

# Register your models here.
admin.site.register(PollModel)
admin.site.register(Comment)