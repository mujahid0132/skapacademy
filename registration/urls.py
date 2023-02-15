from . import views
from django.urls import path
urlpatterns = [
    path('want-a-tutor/', views.want_a_tutor),
    path('become-a-tutor/', views.become_a_tutor),
]
