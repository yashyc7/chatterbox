from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer

@api_view(['GET'])
def get_chat_history(request,room_name):
    messages=Message.objects.filter(room_name=room_name).order_by('timestamp')
    serializer=MessageSerializer(messages,many=True)
    return Response(serializer.data)