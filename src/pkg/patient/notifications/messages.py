from src.pkg.common.notifications.messages import MessageNotification


class PasswordNotification(MessageNotification):
    template_name = 'emails/user/auth/password_set.html'
    subject = 'Password on Doc'


class DoctorConnectionNotification(MessageNotification):
    template_name = 'emails/user/manipulations/doctor_connection.html'
    subject = 'New Doctor on Doc'
