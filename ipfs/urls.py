"""ipfs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),

    # Custom created Urls pointing to each application's url
    path('', include('core.urls')),
    path('login/', include('login.urls', namespace='login')),
    path('register/', include('register.urls')),
    path('upload/', include('upload.urls')),
    path('watch/', include('watch.urls')),
    path('logout/', include('logout.urls')),
    path('activity/', include('like_dislike.urls')),
    path('adadmin/', include('advertisement.urls')),
    path('channel/', include('single_channel.urls')),
    path('like_dislike/', include('like_dislike.urls')),
    path('comments/', include('comments.urls')),
]