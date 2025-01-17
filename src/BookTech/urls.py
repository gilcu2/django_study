from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    path('', include('home.urls')),
    path('movies/', include('movies.urls')),
]
