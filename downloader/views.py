from django.shortcuts import render
from pytube import YouTube
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if request.method == 'POST':
        v_url = request.POST.get('video_url', None)
        yt = YouTube(v_url)
        stream = yt.streams.first()
        stream.download()
        print(v_url)
    return render(request, 'home.html')


# @csrf_exempt
# def download(request):
#     if request.method == 'POST':
#         v_url = request.POST.get('video_url', None)
#         yt = YouTube(v_url)
#         stream = yt.streams.first()
#         stream.download()
#         print(v_url)
#     return render(request, 'home.html', {})
