from django.contrib import admin
from .models import RegisteredMessages

# Register your models here.


@admin.register(RegisteredMessages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'message_url')
    search_fields = ('first_name', 'last_name', 'student_id')
