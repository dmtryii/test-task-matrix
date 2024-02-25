
from django.urls import path

from . import views

urlpatterns = [
    path('matrices/', views.api.urls),
]
