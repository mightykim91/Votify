from django.shortcuts import render, get_object_or_404, redirect
from .models import PollModel
from .forms import PollCreationForm, CommentCreationForm
import random


def index(request):
    polls = PollModel.objects.all()
    top_poll = [0,0]
    for poll in polls:
        total_votes = poll.firstCount + poll.secondCount
        if total_votes > top_poll[1]:
            top_poll[0],top_poll[1] = poll,total_votes
        try:
            poll.firstRatio = (poll.firstCount * 100)//total_votes
            poll.secondRatio = 100-poll.firstRatio

        except ZeroDivisionError:
            poll.firstRatio = 0
            poll.secondRatio = 0

    context = {
        'polls': polls,
        'top_poll': top_poll,
    }
    return render(request, 'poll_manager/index.html', context)


def detail(request, poll_pk):
    poll = get_object_or_404(PollModel, pk=poll_pk)
    total_votes = poll.firstCount + poll.secondCount
    try:
        first_ratio = (poll.firstCount * 100)//total_votes
        second_ratio = 100-first_ratio
    except ZeroDivisionError:
        first_ratio,second_ratio = 0,0

    comment_form = CommentCreationForm()
    comments = poll.comment_set.order_by('-pk')
    context = {
        'poll': poll,
        'comment_form': comment_form,
        'first_ratio': first_ratio,
        'second_ratio': second_ratio,
        'comments': comments,
    }
    return render(request, 'poll_manager/detail.html', context)


def create(request):
    if request.method == "POST":
        form = PollCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poll_manager:index')
    else:
        form = PollCreationForm()
    context = {
        'form': form,
    }
    return render(request,'poll_manager/create.html', context)


def VoteFirst(request, poll_pk):

    poll = get_object_or_404(PollModel, pk=poll_pk)
    poll.firstCount += 1
    poll.save()
    return redirect('poll_manager:detail', poll_pk)


def VoteSecond(request, poll_pk):

    poll = get_object_or_404(PollModel, pk=poll_pk)
    poll.secondCount += 1
    poll.save()
    return redirect('poll_manager:detail', poll_pk)


def PickRandom(request):
    polls = PollModel.objects.all()
    primary_keys = []
    for poll in polls:
        primary_keys.append(poll.pk)

    random_poll = random.choice(primary_keys)
    return redirect('poll_manager:detail',random_poll)


def createComment(request, poll_pk):
    poll = get_object_or_404(PollModel, pk=poll_pk)
    form = CommentCreationForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.poll = poll
        comment.save()
        return redirect('poll_manager:detail', poll_pk)


