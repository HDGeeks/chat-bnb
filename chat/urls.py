#from django.urls import path, re_path
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import MessageViewset, UserViewset,ConversationViewset

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()



router.register(r'user', UserViewset)
router.register(r'chat', ConversationViewset)
router.register(r'message', MessageViewset)

urlpatterns = router.urls
