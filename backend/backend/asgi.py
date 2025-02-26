import os
import django  # Move django import to the top

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()  # Call setup right after setting environment variable

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
