from django.urls import path
from .views import feedback_view, thanks_view

urlpatterns = [
    path('feedback/', feedback_view, name='feedback'),
    path('thanks/', thanks_view, name='thanks'),
]
