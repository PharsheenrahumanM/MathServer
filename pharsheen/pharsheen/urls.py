
from django.contrib import admin
from django.urls import path
from mine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfacearea/', views.surfacearea, name="surfacearea"),
    path('', views.surfacearea, name="surfacearearoot")
]