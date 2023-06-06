import os

from account.models import User
from django.db import migrations


def createsuperuser(apps, schema_editor):
    admin_password = os.environ["ADMIN_PASSWORD"] 
    User.objects.create_superuser("admin", password=admin_password)


class Migration(migrations.Migration):
    
    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(createsuperuser)
    ]