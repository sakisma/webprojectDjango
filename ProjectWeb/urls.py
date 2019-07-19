"""ProjectWeb URL Configuration

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
from django.conf.urls import url
from django.urls import path
from post.views import posts_list,post_details,post_create,post_update,post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', posts_list),
    path('post/create/', post_create),
    path('post/<slug>/', post_details),
    path('post/<slug>/update/', post_update),
    path('post/<slug>/delete/', post_delete)
]
