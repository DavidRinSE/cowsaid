from django.urls import path
from cowsaid import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('history/', views.history, name="history")
]