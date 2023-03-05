from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pixel.urls')),
]


admin.site.site_header = 'Пиксель'
admin.site.site_title = 'Пиксель'
admin.site.index_title = ''