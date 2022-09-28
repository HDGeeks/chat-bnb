from django.urls import path, re_path
from rest_framework import routers

from chat.views import UserViewset,ContactViewset

from chat.views import (ChatCreateView, ChatDeleteView, ChatDetailView,
                    ChatListView, ChatUpdateView)

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete/', ChatDeleteView.as_view())
]


router = routers.SimpleRouter()
#router.register(r'chat', ChatViewset)
router.register(r'user', UserViewset)
router.register(r'contact', ContactViewset)
urlpatterns += router.urls
