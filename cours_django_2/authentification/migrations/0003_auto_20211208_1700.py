# Generated by Django 3.2.9 on 2021-12-08 16:00

from django.db import migrations

# def create_groups(apps, schema_migration, with_create_permissions=True):
#     User = apps.get_model('authentification', 'User')
#     Group = apps.get_model('auth', 'Group')
#     Permission = apps.get_model('auth', 'Permission')

#     add_photo = Permission.objects.get(codename='add_photo')
#     change_photo = Permission.objects.get(codename='change_photo')
#     delete_photo = Permission.objects.get(codename='delete_photo')
#     view_photo = Permission.objects.get(codename='view_photo')

#     creator_permissions = [
#         add_photo,
#         change_photo,
#         delete_photo,
#         view_photo,
#     ]

#     creators = Group(name='creators')
#     creators.save()
#     creators.permissions.set(creator_permissions)

#     subscribers = Group(name='subscribers')
#     subscribers.save()
#     subscribers.permissions.add(view_photo)

#     for user in User.objects.all():
#         if user.role == 'CREATOR':
#             creators.user_set.add(user)
#         if user.role == 'SUBSCRIBER':
#             subscribers.user_set.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0002_rename_progile_photo_user_profile_photo'),
    ]

    operations = [
    ]
