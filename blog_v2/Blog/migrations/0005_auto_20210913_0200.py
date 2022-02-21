# Generated by Django 3.2.6 on 2021-09-13 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0004_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(default='uplodes/profiles/default-profile-pic.jpg', upload_to='uplodes/profiles')),
                ('instagram_url', models.CharField(blank=True, max_length=350, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=350, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=350, null=True)),
                ('website_url', models.CharField(blank=True, max_length=350, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]
