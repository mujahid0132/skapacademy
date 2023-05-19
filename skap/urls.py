from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('shop/',views.home, name="shop"),
    path('blog/', views.blog, name="blog"),
    path('blog/<str:slug>/', views.blog_detail),
    path('<str:db_table>-pdf-download/', views.showdates),
    path('<str:db_table>-pdf-download/<str:date>', views.detail,name="downlad"),
]
