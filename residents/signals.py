from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DocumentRequest, Notification

@receiver(post_save, sender=DocumentRequest)
def notify_resident_on_status_change(sender, instance, created, **kwargs):
    if not created: 
        Notification.objects.create(
            user=instance.user,
            message=f"Ang imong {instance.document_type} kay na-update sa status: {instance.status}."
        )
