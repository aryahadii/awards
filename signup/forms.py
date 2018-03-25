from django import forms
from .models import RegisteredMessages


class MessageRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisteredMessages
        fields = ['first_name', 'last_name', 'student_id', 'message_url']
