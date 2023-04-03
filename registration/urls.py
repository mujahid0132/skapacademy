from . import views
from django.urls import path
urlpatterns = [
    path('find-a-tutor/', views.find_a_tutor),
    path('become-a-tutor/', views.become_a_tutor),
]
