"""trackme URL Configuration

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
from django.urls import path
# urls for manipulating a specific item
# PUT or DELETE /api/v1/items/:id
# urls for general list / post
# POST or GET /api/v1/items/
urlpatterns = [
   
]

from trackmeapp import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index),
    url(
        
        r'^api/v1/items/$',
        views.get_post_items,
        name='get_post_items'
    ),
    url(
    
        r'^api/v1/items/(?P<pk>[0-9]+)$',
        views.update_delete_items,
        name='update_delete_items'
    )

]

