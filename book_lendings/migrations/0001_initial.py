# Generated by Django 5.1.7 on 2025-03-12 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_copies', '0003_alter_bookcopy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_name', models.CharField(max_length=150)),
                ('borrower_email', models.EmailField(max_length=254)),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('returned_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('returned', 'Returned'), ('overdue', 'Overdue')], default='active', max_length=10)),
                ('book_copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_lendings', to='book_copies.bookcopy')),
            ],
        ),
    ]
