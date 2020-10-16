from django.urls import path
from questions import views

urlpatterns = [
    path('', views.questionslist),
    path('advies_formuleren/', views.processing_answers),
]
