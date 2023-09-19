from django.apps import AppConfig

# Register your models here.
class RegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'General register'
    name = 'register'