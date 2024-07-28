from django import forms
from .models import Issue, Status, Type
from django.contrib.auth.models import User

class IssueForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']

class ProjectMemberForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)