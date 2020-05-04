from django import forms
from .models import PollModel, Comment


class PollCreationForm(forms.ModelForm):
    class Meta:
        model = PollModel
        fields = ['first_competitor','second_competitor',]

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','content']