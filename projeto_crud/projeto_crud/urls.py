from django.urls import path
from app_crud import views

urlpatterns = [
    # rota, view, nome para referencia

    path('', views.home, name="home"),
]
