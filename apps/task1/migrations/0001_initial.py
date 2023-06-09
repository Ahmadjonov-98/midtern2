# Generated by Django 4.2 on 2023-05-06 08:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='Username')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, primary_key=True, region='UZ', serialize=False, unique=True, verbose_name='Phone number')),
                ('first_name', models.CharField(max_length=124, verbose_name='First name')),
                ('last_name', models.CharField(max_length=124, verbose_name='Last name')),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is superuser?')),
                ('groups', models.ManyToManyField(blank=True, related_name='task1', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
