"""MySite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from pools import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.show_question, name='show_question'),
    path('question/<int:question_id>/vote>', views.vote, name='vote'),
    path('question/vote/<int:choice_id>', views.vote_choice, name='vote_choice'),
    path('question/<int:question_id>/results', views.show_results, name='show_results'),
    path('question/<int:question_id>/manage', views.manage_question, name='manage_question'),
    path('question/<int:question_id>/manage/close_question', views.close_question, name='close_question'),
    path('question/<int:question_id>/manage/open_question', views.open_question, name='open_question'),
    path('question/manage/remove_choice/<int:choice_id>', views.remove_choice, name='remove_choice'),
]
