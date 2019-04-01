from django.conf.urls import url
from . import consumers

WebSocket_urlpatterns = [
    url(r'^ws/chat/$', consumers.ChatConsumer),
]