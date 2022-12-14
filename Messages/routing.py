from django.urls import path , include
from Messages.consumers import ChatConsumer
 
# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("/messages/" , ChatConsumer.as_asgi()) ,
]