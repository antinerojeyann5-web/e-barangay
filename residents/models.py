from django.db import models
from django.contrib.auth.models import User

class Resident(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DocumentRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DOCUMENT_TYPES = [
        ('Barangay Clearance', 'Barangay Clearance'),
        ('Certificate of Residency', 'Certificate of Residency'),
        ('Certificate of Indigency', 'Certificate of Indigency'),
    ]
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPES)
    purpose = models.TextField()
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Ready for Pickup', 'Ready for Pickup'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.document_type} ({self.status})"

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    details = models.TextField()
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subject} ({self.status})"

# NEW: Rules and Regulations / How to Use Model
class Guide(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="You can use plain text or simple HTML for formatting.")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"
