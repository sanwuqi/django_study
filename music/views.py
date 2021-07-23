from django.shortcuts import render, HttpResponse


# Create your views here.
def index_view(request):
    # return HttpResponse("这是音乐频道首页")
    return render(request, 'music/index.html')
    pass
