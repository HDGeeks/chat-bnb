# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })
from django.urls import path

from chat.consumers import ChatConsumer, NotificationConsumer,NotificationConsumer

websocket_urlpatterns = [ 
    path("chats/<conversation_name>/", ChatConsumer.as_asgi()),
    path("notifications/", NotificationConsumer.as_asgi()),
    
    ]
    