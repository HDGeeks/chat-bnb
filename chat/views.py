from rest_framework.viewsets import ModelViewSet

from .paginator import MessagePagination
from rest_framework.response import Response

from .models import Conversation, Message,User
from .serializers import ConversationSerializer, MessageSerializer,UserSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = User.objects.filter(
                UserId=user).values()
            return Response(queryset)
        else:
            return Response(User.objects.all().values())


class ConversationViewSet(ModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.none()
    lookup_field = "UserId"

    def get_queryset(self):
        queryset = Conversation.objects.filter(
            UserId__contains=self.request['UserId']
        )
        return queryset

    def get_serializer_context(self):
        return {"request": self.request, "user": self.request['UserId']}




class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.none()
    pagination_class = MessagePagination

    def get_queryset(self):
        conversation_name = self.request.GET.get("conversation")
        queryset = (
            Message.objects.filter(
                conversation__name__contains=self.request.user.username,
            )
            .filter(conversation__name=conversation_name)
            .order_by("-timestamp")
        )
        return queryset
