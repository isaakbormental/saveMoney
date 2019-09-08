from django.urls import path
from . import views
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)


urlpatterns = [
    path('', views.ListExpensesView.as_view(), name='index'),
    path('expenses/', views.ListExpensesView.as_view(), name='expenses-list'),
    path('expenses/create', views.ExpenseCreateView.as_view(), name='expenses-create'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('stats/', views.StatsView.as_view(), name='stats'),
]
