# Generated by Django 5.0.4 on 2024-06-07 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('affiliateprogram', '0003_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('invitationid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('invitationimage', models.ImageField(blank=True, upload_to='static/invitationletters')),
                ('invitationstatus', models.CharField(max_length=100)),
                ('invitationuser', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofileinfo')),
            ],
        ),
    ]
