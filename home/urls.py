from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('score/', views.score_view, name='score'),
]