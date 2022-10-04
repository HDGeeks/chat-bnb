from mailbox import Message

from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from chat.models import Conversation, Message, User
from chat.serializers import (ConversationSerializer, MessageSerializer,
                              UserSerializer)


class ConversationViewset(ModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.none()

    def get_queryset(self):
        queryset = Conversation.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.Conversation.all()
        return queryset

class UserViewset(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class MessageViewset(ModelViewSet):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer


    

def get_last_10_messages(chatId):
    chat = get_object_or_404(Conversation, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(username):
    return get_object_or_404(User, UserId=username)
    #return get_object_or_404(Contact, user=user)


def get_current_chat(chatId):
    return get_object_or_404(Conversation, id=chatId)
