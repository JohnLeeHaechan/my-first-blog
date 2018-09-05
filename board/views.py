from django.shortcuts import render
from board.models import Post

# Create your views here.
def mainIndex(request):
    if request.method == 'GET':
        data = Post.objects.all()
        context = {
            'data': data,
        }
        return render(request, 'board/index.html', context)

def detail(request):
    if request.method == 'GET':
        index = request.GET.get('id')
        data = Post.objects.get(id=index)
        data.view_count = data.view_count + 1
        data.save(update_fields=('view_count',))
        context = {
            'data': data,
        }
        return render(request, 'board/detail.html', context)

def photo(request):
    if request.method == 'GET':
        data = Post.objects.all()
        context = {
            'data': data
        }
        return render(request, 'board/photo.html', context)
