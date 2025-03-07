from django.http import JsonResponse
from django.shortcuts import render
import time

def index(request):
    """Render the HTML page."""
    return render(request, "streamapp/index.html")

def stream_hello_world(request):
    """Returns a JSON response with a new message on each request."""
    return JsonResponse({
        "message": time.strftime('%H:%M:%S')
    })
