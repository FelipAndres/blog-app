from django.urls import path
from .views import EntradaView

urlpatterns = [
    path('', EntradaView.as_view()),]
