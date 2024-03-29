from django.conf.urls import include, url
from django.contrib import admin


from tags.views import (
        TagListView,
        TagDetailView

)


urlpatterns = [
    url(r'^$', TagListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', TagDetailView.as_view(), name='detail'),

]
