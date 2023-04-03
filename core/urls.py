from django.contrib import admin
from django.urls import path , include , re_path
from django.views.static import serve 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include("ecommerce.urls"),name="shop"),
    path('', include("skap.urls")),
    path('registration/', include("registration.urls")),
    path('lms/', include("lms.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
