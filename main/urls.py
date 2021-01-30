from django.urls import path
from main.views import *

urlpatterns = [
    path('', OpportunityListView.as_view(), name='opportunity-list'),
    path('account/', AccountListView.as_view(), name='accounts_list'),
    path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('account/new/', AccountCreateView.as_view(), name='account-create'),
    path('account/<int:pk>/update/', AccountUpdateView.as_view(), name='account-update'),
    path('account/<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),
    path('create_opportunity/<int:pk>/', create_opportunity, name="create-opportunity"),
    path('opportunity/<int:pk>/', OpportunityDetailView.as_view(), name='opportunity-detail'),
    path('opportunity/<int:pk>/update/', OpportunityUpdateView.as_view(), name='opportunity-update'),
    path('opportunity/<int:pk>/delete/', OpportunityDeleteView.as_view(), name='opportunity-delete'),
    path('register/', register, name='register'),
]