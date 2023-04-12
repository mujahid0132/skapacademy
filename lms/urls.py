from . import views
from django.urls import path
urlpatterns = [
    path('lms-request/', views.lms_request),
]
