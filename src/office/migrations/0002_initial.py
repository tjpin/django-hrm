# Generated by Django 4.1.7 on 2023-04-01 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='trainees',
            field=models.ManyToManyField(to='staff.staff'),
        ),
        migrations.AddField(
            model_name='performance',
            name='evaluator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance_evaluator', to='staff.hod'),
        ),
        migrations.AddField(
            model_name='performance',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_performance', to='staff.staff'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff'),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.staff'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcement',
            name='target',
            field=models.ManyToManyField(to='office.department'),
        ),
    ]