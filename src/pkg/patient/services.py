from django.contrib.auth import get_user_model

# from pkg.patient.notifications.service import UserNotifications


class PatientService:

    # email_service = UserNotifications()

    @staticmethod
    def register(email, password, first_name, last_name, **extra_fields):
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        # if not is_active:
        #     UserService.email_service.send_user_activation(user)
        # else:
        #     UserService.email_service.success_register_to_user(user)

        return user

    # @staticmethod
    # def activate(user):
    #     user.is_active = True
    #     user.save()
    #
    #     UserService.email_service.success_register_to_user(user)
    #     return user
