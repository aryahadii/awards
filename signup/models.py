from django.db import models

from django.utils.translation import ugettext_lazy as _


class RegisteredMessages(models.Model):
    first_name = models.CharField(
        verbose_name=_('First Name'), max_length=100, null=False)
    last_name = models.CharField(
        verbose_name=_('Last Name'), max_length=100, null=False)
    student_id = models.CharField(
        verbose_name=_('Student ID'), max_length=7, null=False)
    message_url = models.URLField(
        verbose_name=_('Message URL'), max_length=256, null=False)
