from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^lists/$',views.ShowLists,name='lists'),
    url(r'^items/$',views.ShowItems,name='items'),
    url(r'^lists/(?P<id>[0-9]+)/$',views.ShowItems,name='lists_id'),
    #url(r'^items/(?P<id>[0-9]+)/$', views.ShowItemsId, name='items_id'),
    url(r'^lists/create/$',views.CreateList.as_view(),name='create_list'),
    url(r'^lists/delete/(?P<pk>[0-9]+)/$',views.DeleteList.as_view(),name='delete_list'),
    url(r'^lists/update/(?P<pk>[0-9]+)/$',views.UpdateList.as_view(),name='update_list'),

    ###--Rest_Apis--###
    url(r'^rest/lists/$',views.rest_lists.as_view(), name="rest_lists"),
    url(r'^rest/lists/(?P<pk>[0-9]+)/$', views.rest_lists_id.as_view() ,name='rest_lists_id'),
    url(r'^rest/items/$',views.rest_items.as_view(), name='rest_items'),
    url(r'^rest/items/(?P<pk>[0-9]+)/$', views.rest_items_id.as_view(), name='rest_lists_id'),
    url(r'^rest/lists/(?P<list_id>[0-9]+)/items/(?P<item_id>[0-9]+)/$',views.rest_list_id_items_id.as_view(),name='rest_list_id_item_id'),
    url(r'^rest/lists/(?P<list_id>[0-9]+)/items/$', views.rest_list_id_items.as_view(),name='rest_list_id_items'),

    ###-Page-###
    url(r'^home/$',views.HomeLists,name="home")
]