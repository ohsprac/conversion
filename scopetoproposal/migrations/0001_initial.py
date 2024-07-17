# Generated by Django 5.0.7 on 2024-07-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(blank=True, default='', max_length=100)),
                ('contact_person', models.CharField(blank=True, default='', max_length=100)),
                ('contact_email', models.EmailField(blank=True, default='', max_length=100)),
                ('contact_number', models.CharField(blank=True, default='', max_length=100)),
                ('industry', models.CharField(choices=[('N', 'None'), ('Con', 'Construction'), ('Com', 'Commercial'), ('Eng', 'Eergy'), ('Pet', 'PetroChemical')], default='N', max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]