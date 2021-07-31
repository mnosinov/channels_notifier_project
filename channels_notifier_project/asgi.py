import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from notifier.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_notifier_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(ws_urlpatterns)
})
