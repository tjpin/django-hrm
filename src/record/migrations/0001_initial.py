# Generated by Django 4.1.7 on 2023-04-01 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to='records/uploads')),
                ('date_uploaded', models.DateField(default=django.utils.timezone.now)),
                ('reference_number', models.CharField(default=5612485373, max_length=10, unique=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_uploaded', 'uploaded_by'],
            },
        ),
        migrations.CreateModel(
            name='Transmital',
            fields=[
                ('transmital_number', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('date_sent', models.DateField(default=django.utils.timezone.now)),
                ('date_returned', models.DateField(blank=True, null=True)),
                ('is_returned', models.BooleanField(blank=True, default=False, null=True)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Recived', 'Recived'), ('Transmited', 'Transmited')], default='Transmited', max_length=15)),
                ('reason_for_transmital', models.CharField(choices=[('For Distribution', 'For Distribution'), ('For Assesment', 'For Assesment'), ('For Disposal', 'For Disposal'), ('For Archive', 'For Archive'), ('For Approved', 'For Approved')], default='For Approved', max_length=30)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.document')),
                ('sent_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sent_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
            options={
                'ordering': ['date_sent', 'transmital_number', 'status'],
            },
        ),
    ]
