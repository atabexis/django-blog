from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.post_list, name='post_list'),
    path('authors/', views.author_list, name='author_list'),
    path('login/', views.user_login, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)