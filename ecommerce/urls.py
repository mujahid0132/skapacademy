from . import views
from django.urls import path
urlpatterns = [
    path('', views.shop),
    path('products/', views.products),
    path('products/<str:slug>/', views.productdetail),
    path('checkout/', views.checkout),
    path('complete/', views.complete_order),
    path('test/', views.test),
    path('request-a-book/', views.request_a_book),
    path('<str:db_table>-pdf-download/', views.showdates),
    path('<str:db_table>-pdf-download/<str:date>', views.detail,name="downlad"),
    # path('testees/', views.generate_pdf),
]
