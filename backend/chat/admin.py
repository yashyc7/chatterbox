from django.contrib import admin
from .models import Message  # Import your chat model

@admin.register(Message)  # Use this instead of admin.site.register
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room_name', 'content','timestamp')  # Customize fields shown in the admin panel
    search_fields = ('user__username', 'content')  # Enable searching
    list_filter = ('timestamp',)  # Add filtering by date

# If using a different model, replace `ChatMessage` with your model name
