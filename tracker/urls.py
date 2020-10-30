"""expenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tracker.views.expense_views import create_expense_view, edit_expense_view, delete_expense_view
from tracker.views.profile_views import home_page_view, profile_view

urlpatterns = [
    path('', home_page_view, name='home page'),
    path('create/', create_expense_view, name='create expense'),
    path('edit/<int:my_id>/', edit_expense_view, name='edit expense'),
    path('delete/<int:my_id>/', delete_expense_view, name='delete expense'),
    # profile views
    path('profile', profile_view, name='profile view'),

]
