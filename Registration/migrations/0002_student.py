# Generated by Django 4.0.5 on 2023-08-29 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.course')),
            ],
        ),
    ]
