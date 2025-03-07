import time
from django.http import StreamingHttpResponse
from django.shortcuts import render

def event_stream():
    # """Generator function to send data to client"""
    while True:
        yield f"data: {time.strftime('%H:%M:%S')}\n\n"
        time.sleep(1) 

def sse_view(request):
    # """Django view to handle SSE"""
    response = StreamingHttpResponse(
        event_stream(), 
        content_type='text/event-stream'
    )
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'
    return response

def index(request):
    return render(request, 'index.html')
