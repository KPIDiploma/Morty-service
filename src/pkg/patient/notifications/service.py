from django.contrib.auth.tokens import default_token_generator

from src.pkg.patient.notifications.messages import PasswordNotification, \
    DoctorConnectionNotification
from src.pkg.common.notifications.base import EmailNotification
from src.pkg.patient.utils import encode_uid


class UserNotifications(EmailNotification):
    @staticmethod
    def _get_data(user, **kwargs):
        data = {
            'user': user,
            'uid': encode_uid(user.pk),
            'token': default_token_generator.make_token(user),
        }
        data.update(**kwargs)
        return data

    # def send_user_activation(self, user):
    #     user_data = self._get_data(user)
    #     user_data.update({
    #         'url': settings.ACTIVATION_URL.format(**user_data)
    #     })
    #
    #     message = ActivateUserMessage(**user_data)
    #     self.service.send_to_user(message, user.email)
    #
    # def send_reset_password_link(self, user):
    #     user_data = self._get_data(user)
    #     user_data.update({
    #         'url': settings.PASSWORD_RESET_CONFIRM_URL.format(**user_data)
    #     })
    #
    #     message = PasswordResetMessage(**user_data)
    #     self.service.send_to_user(message, user.email)
    #
    # def success_register_to_user(self, user):
    #     message = SuccessRegisterUserMessage(user=user)
    #     self.service.send_to_user(message, user.email)

    def send_password_to_user(self, user, password):
        message = PasswordNotification(user=user, password=password)
        self.service.send_to_user(message, user.email)

    def send_doctor_connection(self, user, link, doctor_fullname):
        message = DoctorConnectionNotification(link=link,
                                               doctor_fullname=doctor_fullname)
        self.service.send_to_user(message, user.email)
