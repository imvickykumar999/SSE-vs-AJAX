from django.urls import path
from .views import index, stream_hello_world

urlpatterns = [
    path('', index, name='index'),
    path('stream/', stream_hello_world, name='stream_hello_world'),
]
