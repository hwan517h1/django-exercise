from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'WebSocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.WebSocket_urlpatterns
        )
    ),
})