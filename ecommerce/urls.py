from . import views
from django.urls import path
urlpatterns = [
    path('', views.shop),
    path('products/', views.products),
    path('products/<str:slug>/', views.productdetail),
    path('checkout/', views.checkout),
    path('complete/', views.complete_order),
    path('request-a-book/', views.request_a_book),
]
