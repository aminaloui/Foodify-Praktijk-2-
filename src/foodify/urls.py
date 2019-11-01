"""foodify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from foods.views import (
        FoodCreateView,
        FoodDetailView, FoodListView,
        FoodUpdateView
        )

from tags.views import (
        TagListView,
        TagDetailView

)
from dashboard.views import DashboardView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/$', 'foods.views.create_view', name='create_view'),
    url(r'^detail/(?P<object_id>\d+)/$', 'foods.views.detail_view', name='detail_view'),
    url(r'^detail/(?P<object_id>\d+)/edit/$', 'foods.views.update_view', name='update_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', 'foods.views.detail_slug_view', name='detail_slug_ view'),
    url(r'^list/$', 'foods.views.list_view', name='list_view'),
    url(r'^foods/$', FoodListView.as_view(), name='foods_list_view'),
    url(r'^foods/add/$', FoodCreateView.as_view(), name='food_create_view'),
    url(r'^foods/(?P<pk>\d+)/$', FoodDetailView.as_view(), name='food_detail_view'),
    url(r'^foods/(?P<slug>[\w-]+)/$', FoodDetailView.as_view(), name='food_detail_slug_view'),
    url(r'^foods/(?P<pk>\d+)/edit/$', FoodUpdateView.as_view(), name='food_update_view'),
    url(r'^foods/(?P<slug>[\w-]+)/edit/$', FoodUpdateView.as_view(), name='food_update_view'),

    url(r'^tags/', include("tags.urls", namespace='tags')),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)