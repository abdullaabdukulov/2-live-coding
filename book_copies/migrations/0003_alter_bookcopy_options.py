# Generated by Django 5.1.7 on 2025-03-12 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_copies', '0002_alter_bookcopy_condition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcopy',
            options={'verbose_name': 'Book Copy', 'verbose_name_plural': 'Book Copies'},
        ),
    ]
