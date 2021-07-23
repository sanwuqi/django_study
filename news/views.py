from django.shortcuts import render, HttpResponse


# Create your views here.
def index_view(request):
    # return HttpResponse("这里是新闻频道首页")
    return render(request, 'news/index.html')
