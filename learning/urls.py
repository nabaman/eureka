from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


urlpatterns = [
    path('',login_required(dashboardView,login_url='login'), name='dashboard'),
    path('assignment/',login_required(assignmentView,login_url='login'), name='assignment'),
    path('create-assignment/',createAssignment, name='create-assignment'),
    path('list-question/<int:pk>/',listQuestion,name='list-question'),
    path('add-materi/<int:pk>/', addMateri, name='add-materi'),
    path('add-question/<int:pk>/',addQuestion, name='add-question')
]

