from django.urls import path


from .consumers import StatusConsumer


ws_urlpatterns = [
    path('ws/status/', StatusConsumer.as_asgi()),
]
