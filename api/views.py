from rest_framework import routers, viewsets
from rest_framework import permissions
from .serializers import UserSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.models import ChatUser, Message
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = ChatUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

@api_view(['GET'])
def get_current_user(request):
    data = request.user
    if not data.is_authenticated:
        data = {'username': 'DUMMYUSER', 'is_staff': False}
        return Response(data)
    serializer = UserSerializer(data, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_messages(request):
    user = request.user
    reciever = request.query_params.get('reciever')
    if not user.is_authenticated:
        sender = ChatUser.objects.get(username='jenish')
        reciever = ChatUser.objects.get(username='junky')
        sender_to_reciever = Message.objects.filter(sender=sender, reciever=reciever)
        reciever_to_sender = Message.objects.filter(sender=reciever, reciever=sender)
        msg = sender_to_reciever | reciever_to_sender   #combining the two results
        msg = msg.order_by('created_at')
        message = []
        for i in msg:
            if i.sender == sender:
                message.append({'sender': sender.username, 'reciever': reciever.username, 'content': i.content, 'created_at': i.created_at})
            else:
                message.append({'sender': reciever.username, 'reciever': sender.username, 'content': i.content, 'created_at': i.created_at})
        return Response(message)
    
    reciever = ChatUser.objects.get(username=reciever)
    sender_to_reciever = Message.objects.filter(sender=user, reciever=reciever)
    reciever_to_sender = Message.objects.filter(sender=reciever, reciever=user)
    msg = sender_to_reciever | reciever_to_sender   #combining the two results
    msg = msg.order_by('created_at')
    message = []
    for i in msg:
        if i.sender == user:
            message.append({'sender': user.username, 'reciever': reciever.username, 'content': i.content, 'created_at': i.created_at})
        else:
            message.append({'sender': reciever.username, 'reciever': user.username, 'content': i.content, 'created_at': i.created_at})
    serializer = MessageSerializer(msg, many=True, context={'request': request})
    return Response(message)

@api_view(['GET'])
def get_chats(request):
    user = request.user
    if not user.is_authenticated:
        user = ChatUser.objects.get(username='jenish')

        msg = organise_chats(user)
        print(msg)
                
        return Response(msg)
    msg = organise_chats(user)
    #serializer = MessageSerializer(msg, many=True, context={'request': request})
    return Response(msg)

def organise_chats(user):
    chat_fromOthers = Message.objects.filter(reciever=user).order_by('created_at')
    chat_toOthers = Message.objects.filter(sender=user).order_by('created_at')
    chats = chat_fromOthers | chat_toOthers
    chats = chats.order_by('created_at')
    found_users = {}
    msg = []

    for i in chats[::-1]:
        if user == i.sender:
            if i.reciever not in found_users:
                msg.append({'user': i.reciever.username, 'content': i.content, 'created_at': i.created_at})
                found_users[i.reciever] = msg[-1]
            else:
                message = found_users[i.reciever]
                if i.created_at > message['created_at']:
                    message['content'] = i.content
                    message['created_at'] = i.created_at
        elif user == i.reciever:
            if i.sender not in found_users:
                msg.append({'user': i.sender.username, 'content': i.content, 'created_at': i.created_at})
                found_users[i.sender] = msg[-1]
            else:
                message = found_users[i.sender]
                if i.created_at > message['created_at']:
                    message['content'] = i.content
                    message['created_at'] = i.created_at
    return msg

    

@api_view(['GET'])
def search_user(request):
    user = request.user
    search_text = request.query_params['search_text']
    users = ChatUser.objects.filter(username=search_text)
    serializer = UserSerializer(users, many=True, context={'request': request})
    return Response(serializer.data)
    