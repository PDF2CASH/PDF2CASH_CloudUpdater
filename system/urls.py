from django.conf.urls import url
from .views import SystemView

urlpatterns = [
    url(r'^system/(?P<services>[^/]+)/$',SystemView.as_view())
]
