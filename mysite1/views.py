from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render


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