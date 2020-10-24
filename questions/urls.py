from django.urls import path
from questions import views

urlpatterns = [
    path('', views.questionslist),
    # path('<str:username>', views.questionslist),
    path('advies_formuleren/<str:username>/', views.processing_answers),
]
