from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import hrm_app.settings as sett

from apps.corecode.models import PermitDocCategory, Citizenship


class Employee(models.Model):
    STATUS_CHOICES = [("active", "active"), ("inactive", "inactive")]

    GENDER_CHOICES = [("male", "male"), ("female", "female")]

    #STAFF_CHOICES = [("WhiteCollar", "Белый воротник"), ("BlueCollar", "Синий воротник")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", verbose_name="Status"
    )
    personnel_number = models.CharField(max_length=200, unique=True, verbose_name="Personnel Number")
    surname = models.CharField(max_length=200, verbose_name="Surname")
    firstname = models.CharField(max_length=200, verbose_name="Name")
    other_name = models.CharField(max_length=200, blank=True, verbose_name="Surname")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male", verbose_name="Floor")
    date_of_birth = models.DateField(default=timezone.now, verbose_name="Date of Birth")
    position = models.CharField(max_length=200, verbose_name="Job title")
    """ current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    ) """
    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Citizenship"
    )

    current_doc_category = models.ForeignKey(
        PermitDocCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document category"
    )
    date_of_employment = models.DateField(default=timezone.now, verbose_name="date of receipt")

    date_of_dismissal = models.DateField(verbose_name="Date of dismissal")

    tin_number = models.CharField(max_length=200, blank=True, verbose_name="TIN")

    snils_number = models.CharField(max_length=200, blank=True, verbose_name="SNILS")

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True, verbose_name="Tel number"
    )

    address = models.TextField(blank=True, verbose_name="Address in the Russian Federation")
    others = models.TextField(blank=True, verbose_name="Other")
    photo = models.ImageField(blank=True, upload_to="employees/photos/", verbose_name="Photo")

    class Meta:
        ordering = ["personnel_number", "surname", "firstname", "other_name"]

    def __str__(self):
        #return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"
        return "{} {} {} ({})".format(self.surname, self.firstname, self.other_name, self.personnel_number)

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})


class EmployeeBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="employees/bulkupload/")
