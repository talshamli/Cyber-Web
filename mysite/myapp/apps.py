from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

class ChangepasswordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'changepassword'