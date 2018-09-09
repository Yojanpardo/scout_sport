from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('cazatalentos/',include('cazatalentos.urls',namespace='cazatalentos')),
    path('clubs/',include('clubs.urls',namespace='clubs')),
    path('deportistas/',include('deportistas.urls',namespace='deportistas')),
    path('deportes/',include('sports.urls',namespace='deportes')),
]
