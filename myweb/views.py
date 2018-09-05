from django.shortcuts import render, HttpResponse

# Create your views here.
def mainIndex(request):

    return render(request, 'myweb/index.html')

def fileIndex(request):
    return HttpResponse("<img src='{{ url:file }}'>")
