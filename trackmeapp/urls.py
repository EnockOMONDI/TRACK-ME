from django.contrib import admin
# urls for manipulating a specific item
# PUT or DELETE /api/v1/items/:id
# urls for general list / post
# POST or GET /api/v1/items/


from trackmeapp import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [

    path('', views.index),
    url(r'^api/v1/items/$',views.get_post_items,name='get_post_items'),
    url(r'^api/v1/items/(?P<pk>[0-9]+)$', views.update_delete_items,name='update_delete_items')
    
]