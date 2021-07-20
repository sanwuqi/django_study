from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def page_2003_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def index_view(request):
    html = "这是我的首页"
    return HttpResponse(html)


def page1_view(request):
    html = "这是我的第一个页面"
    return HttpResponse(html)


def page2_view(request):
    html = "这是我的第二个页面"
    return HttpResponse(html)


def pages_view(request, pg):
    html = f"这是我的第{pg}个页面"
    return HttpResponse(html)


def test_html(request):
    # t = loader.get_template('test_html.html')
    # html = t.render()
    dic = {'username': 'xiaonao', 'age': 18}
    return render(request, 'test_html.html', dic)
    # return HttpResponse(html)
    pass


def test_if_for(request):
    dic = dict()
    dic['x'] = 10
    return render(request, 'test_if_for.html', dic)


@csrf_exempt
def test_mycal(request):
    if request.method == "GET":
        return render(request, 'mycal.html')
    elif request.method == "POST":
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op == "add":
            result = x + y
        elif op == "sub":
            result = x - y
        elif op == "mul":
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'mycal.html', locals())


def base_view(request):
    lst = ['tom', 'Jack']
    return render(request, 'base.html', locals())


def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')
