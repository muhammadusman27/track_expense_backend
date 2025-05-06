# audit/signals.py
from django.contrib.contenttypes.models import ContentType
from logs.models import AuditLog
from logs.middleware import get_current_user
from django.db.models import ForeignKey



def track_model_changes(sender, instance, **kwargs):
    if not instance.pk:
        return  # Skip new objects

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    changes = {}
    for field in sender._meta.fields:
        field_name = field.name
        old_value = getattr(old_instance, field_name, None)
        new_value = getattr(instance, field_name, None)

        if isinstance(field, ForeignKey):
            old_repr = str(old_value) if old_value else None
            new_repr = str(new_value) if new_value else None

            if old_value != new_value:
                changes[field_name] = {
                    "old_id": old_value.pk if old_value else None,
                    "new_id": new_value.pk if new_value else None,
                    "old_repr": old_repr,
                    "new_repr": new_repr,
                }
        else:
            if old_value != new_value:
                changes[field_name] = {
                    "old_value": str(old_value),
                    "new_value": str(new_value),
                }

    if changes:  # Only log if something actually changed
        AuditLog.objects.create(
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
            changes=changes,
            changed_by=get_current_user()
        )
