from django.apps import AppConfig

class LocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'location'

    def ready(self):
        import location.signals  # Ensure signals are loaded
