from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView
from .views import AddUserToIssueView, RemoveUserFromIssueView
from . import views
urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/edit/<int:pk>/', IssueUpdateView.as_view(), name='issue_edit'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='issue_delete'),
    path('issues/<int:issue_id>/add_user/', AddUserToIssueView.as_view(), name='add_user_to_issue'),
    path('issues/<int:issue_id>/remove_user/', RemoveUserFromIssueView.as_view(), name='remove_user_from_issue'),
    path('', views.HomeView.as_view(), name='home'),
]