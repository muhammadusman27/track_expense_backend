from django.apps import AppConfig



class LogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logs'


    def ready(self):
        
        # Delayed import to avoid AppRegistryNotReady
        from django.apps import AppConfig, apps
        from django.db.models.signals import pre_save
        from logs.signals import track_model_changes


        # Avoid circular imports
        from django.db.models import Model

        # Loop over all models in all installed apps
        for model in apps.get_models():
            if model.__name__ == 'AuditLog':
                continue  # skip logging itself

            # Connect pre_save to our handler
            pre_save.connect(track_model_changes, sender=model, dispatch_uid=f"{model.__name__}_change_tracker")