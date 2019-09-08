from django.urls import path
from . import views
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)


urlpatterns = [
    path('month/categories', views.MonthsCatsView.as_view(), name='month-categories'),
]