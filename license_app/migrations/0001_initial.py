# Generated by Django 4.2.10 on 2024-02-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('licence_key', models.CharField(max_length=16)),
                ('pcname', models.CharField(max_length=255)),
                ('lic_used', models.BooleanField(default=False)),
                ('lic_active', models.BooleanField(default=False)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('activate_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='license_app.product')),
            ],
        ),
    ]
