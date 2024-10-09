# Generated by Django 4.2.16 on 2024-10-08 10:27

import books_app.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('nationality', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published_year', models.IntegerField()),
                ('genre', models.CharField(max_length=255, null=True)),
                ('isbn', models.CharField(max_length=13, unique=True, validators=[books_app.models.validate_fixed_length])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('return_date', models.DateTimeField(null=True)),
                ('reated', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='books_app.book')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered as 9 to 10 digits (e.g., '1234567890').", regex='^\\d{9,10}$')])),
                ('address', models.CharField(max_length=255, null=True)),
                ('membership_date', models.DateTimeField(null=True)),
                ('membership_status', models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive')], default='AC', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fine_amount', models.IntegerField()),
                ('fine_status', models.CharField(choices=[('RE', 'RETURNED'), ('NOT RE', 'NOT RETURNED')], default='NOT RE', max_length=7)),
                ('reated', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('borrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_app.borrowing')),
            ],
        ),
        migrations.AddField(
            model_name='borrowing',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_app.member'),
        ),
    ]
