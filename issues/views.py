from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjectMemberForm
from django.views import View
from .models import Issue
from .forms import IssueForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView

class IssueListView(LoginRequiredMixin, ListView):

    model = Issue
    template_name = 'issues/issue_list.html'

class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_form.html'
    success_url = reverse_lazy('issue_list')

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_form.html'
    success_url = reverse_lazy('issue_list')

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issues/issue_confirm_delete.html'
    success_url = reverse_lazy('issue-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = self.get_object()

        if not self.request.user.has_perm('issues.add_user_to_issue'):
            return HttpResponseForbidden("У вас нет разрешения на добавление пользователей в проект.")

        context['users'] = User.objects.all()
        return context
    
class AddUserToIssueView(View):
    def post(self, request, issue_id):
        issue = get_object_or_404(Issue, id=issue_id)
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        issue.users.add(user)
        return redirect('issue_detail', issue_id=issue.id)

class RemoveUserFromIssueView(View):
    def post(self, request, issue_id):
        issue = get_object_or_404(Issue, id=issue_id)
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        issue.users.remove(user)
        return redirect('issue_detail', issue_id=issue.id)
    
class HomeView(TemplateView):
    template_name = 'home.html'