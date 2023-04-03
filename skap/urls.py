from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('success/', views.about, name="success"),
    path('contact/', views.contact, name="contact"),
    path('shop/',views.home, name="shop"),
    path('blog/', views.blog, name="blog"),
    path('<str:db_table>-pdf-download/', views.showdates),
    path('<str:db_table>-pdf-download/<str:date>', views.detail,name="downlad"),
]
