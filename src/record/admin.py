from django.contrib import admin

from .models import Document, Transmital


@admin.register(Transmital)
class TransmitalAdmin(admin.ModelAdmin):
    list_display = ['transmital_number', 'sent_by', 'sent_to', 'date_sent', 'returned', 'status', 'reason_for_transmital']

    def returned(self, obj):
        if obj.is_returned:
            return "Returned"
        return "Pending"

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['filename', 'reference_number', 'date_uploaded', 'uploaded_by']

