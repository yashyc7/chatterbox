from django.urls import path
from views import get_chat_history

urlpatterns=[
    path('history/<str:room_name>/',get_chat_history,name='chat-history')
]