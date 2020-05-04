from django.db import models

# Create your models here.
class PollModel(models.Model):
    first_competitor = models.CharField(max_length=100)
    second_competitor = models.CharField(max_length=100)
    firstCount = models.PositiveIntegerField(default=0)
    secondCount = models.PositiveIntegerField(default=0)
    firstRatio = models.PositiveIntegerField(default=0)
    secondRatio = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    name = models.CharField(help_text='please provide your nick name', max_length=50)
    content = models.CharField(verbose_name='comment', max_length=150,help_text='type your opinion')
    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE)
