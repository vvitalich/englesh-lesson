from django.urls import path
from .views import WorldView

urlpatterns = [
    path('', WorldView.as_view(), name='world'),
]