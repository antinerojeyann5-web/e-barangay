from django.contrib import admin
from .models import Resident, DocumentRequest, Announcement, Complaint, Guide

admin.site.register(Resident)
admin.site.register(DocumentRequest)
admin.site.register(Announcement)
admin.site.register(Complaint)
admin.site.register(Guide)