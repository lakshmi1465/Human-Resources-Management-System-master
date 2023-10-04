from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import hrm_app.settings as sett

from apps.corecode.models import Citizenship, DocumentType
from apps.employees.models import Employee

# Create your models here.

class Doc(models.Model):
    STATUS_CHOICES = [("active", "active"), ("inactive", "inactive")]

    #GENDER_CHOICES = [("male", "Муж"), ("female", "Жен")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", verbose_name="Status"
    )

    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee"
    )

    doc_type = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document type"
    )

    serial = models.CharField(max_length=200, verbose_name="Series") # unique=True,
    number = models.CharField(max_length=200, verbose_name="Number No.")

    date_of_issue = models.DateField(default=timezone.now,  verbose_name="date of issue")
    date_of_preparing = models.DateField(default=timezone.now, verbose_name="Start ordering before")
    date_of_expiry = models.DateField(default=timezone.now, verbose_name="Valid until")

    issued_authority = models.CharField(max_length=200, verbose_name="Issued by")

    address = models.TextField(blank=True, verbose_name="Address in the Russian Federation")
    others = models.TextField(blank=True, verbose_name="Other")
    scanned_doc = models.FileField(blank=True, upload_to="docs/uploads/", verbose_name="Upload file")

    class Meta:
        ordering = ["current_status"]

    def __str__(self):
        return "{} - {}".format(self.doc_type, self.employee)

    def get_absolute_url(self):
        return reverse("doc-detail", kwargs={"pk": self.pk})

class DocBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="docs/bulkupload/")
