from django.shortcuts import render, HttpResponse


# Create your views here.
def index_view(request):
    # return HttpResponse("这里是体育频道")
    return render(request, 'sport/index.html')
