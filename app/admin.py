from django.contrib import admin
from .models import Candidate
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class CandidateResource(resources.ModelResource):
    class Meta:
        model = Candidate
class CandidateAdmins(ImportExportModelAdmin):
    resource_class = CandidateResource
    list_display=("id","name")
admin.site.register(Candidate,CandidateAdmins)