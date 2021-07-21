"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('page/2003/', views.page_2003_view),
    path('page/<int:pg>', views.pages_view),
    # path('page/2', views.page2_view),
    path('test_html', views.test_html),
    path('test_if_for', views.test_if_for),
    path('mycal', views.test_mycal),
    path('base_index', views.base_view, name='base_index'),
    path('music_index', views.music_view),
    path('sport_index', views.sport_view),
    path('test/url', views.test_url),
    path('test_urls_result/<int:age>', views.test_url_result, name="tr"),
    path('test_static', views.test_static, ),
    path('music/', include('music.urls')),
    path('news/', include('news.urls')),
    path('sport/', include('sport.urls')),
]
