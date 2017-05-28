from src.pkg.common.notifications.messages import MessageNotification


class PasswordNotification(MessageNotification):
    template_name = 'emails/user/auth/password_set.html'
    subject = 'Password on Ambulatoria'


class DoctorConnectionNotification(MessageNotification):
    template_name = 'emails/user/manipulations/doctor_connection.html'
    subject = 'New Doctor on Ambulatoria'


class NewDiagnoseNotification(MessageNotification):
    template_name = 'emails/user/manipulations/new_diagnose.html'
    subject = 'New Diagnose on Ambulatoria'


class UpdateDiagnoseNotification(MessageNotification):
    template_name = 'emails/user/manipulations/update_diagnose.html'
    subject = 'Diagnose was updated on Ambulatoria'

