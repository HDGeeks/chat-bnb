#from django.urls import path, re_path
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import UserViewset,MessageViewSet,ConversationViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()



router.register(r'user', UserViewset)
router.register(r'conversation', ConversationViewSet)
router.register(r'message', MessageViewSet)

urlpatterns = router.urls
