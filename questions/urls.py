from django.urls import path
from questions import views

urlpatterns = [
    path('', views.questionslist),
    # path('/resultaten/<str:username>/', views.show_results),
    path('advies_formuleren/<str:username>/', views.processing_answers),
]
