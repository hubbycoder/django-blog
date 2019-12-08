from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def reday(self):
        import users.signals        