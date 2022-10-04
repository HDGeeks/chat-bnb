from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from chat import routing
from .wsgi import get_wsgi_application

from .websocket import websocket_application

django_application=get_asgi_application
async def application(scope, receive, send):
    if scope["type"] == "http":
        await django_application(scope, receive, send)
    elif scope["type"] == "websocket":
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(routing.websocket_urlpatterns),
})
