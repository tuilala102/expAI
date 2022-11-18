from rest_framework.serializers import ModelSerializer
from .models import *

class SoftwareLibsSerializer(ModelSerializer):
    class Meta:
    #         softwarelibid = models.CharField(db_column='softwarelibID', primary_key=True, max_length=20)  # Field name made lowercase.
    # softwarelibname = models.CharField(db_column='softwarelibName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # softwareliburl = models.CharField(db_column='softwarelibURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # softwarelibdescription = models.CharField(db_column='softwarelibDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.

        model = Softwarelibs
        fields = ["softwarelibid","softwarelibname","softwareliburl","softwarelibdescription"]

