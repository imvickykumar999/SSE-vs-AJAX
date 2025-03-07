from django.urls import path
from .views import sse_view, index

urlpatterns = [
    path('', index, name='home'),
    path('events/', sse_view, name='sse_view'),
]
