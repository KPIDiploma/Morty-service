import re

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail


class EmailService:
    plain = re.compile(r'<.*?>')

    def _send_email(self, subject, message, email):
        from_email = settings.DEFAULT_FROM_EMAIL
        plain_message = self.plain.sub('', message)
        send_mail(
            subject,
            plain_message,
            from_email,
            [email],
            html_message=message)

    def process_email(self, email, msg, subject=''):
        message = self._get_message(msg)
        sbj = self._get_subject(msg, subject)
        self._send_email(sbj, message, email)

    def send_to_user(self, msg, email, subject=''):
        self.process_email(email, msg, subject)

    def send_to_admin(self, msg, subject=''):
        admins = getattr(settings, 'ADMINS', [])
        for name, email in admins:
            self.process_email(email, msg, subject)

    def send_to_superusers(self, msg, subject=''):
        admins = User.objects.filter(
            is_staff=True, is_active=True).exclude(email='')
        for user in admins:
            self.process_email(user.email, msg, subject)

    @staticmethod
    def _get_message(email_message):
        return email_message.get_content()

    @staticmethod
    def _get_subject(email_message, subject=''):
        return email_message.get_subject()
