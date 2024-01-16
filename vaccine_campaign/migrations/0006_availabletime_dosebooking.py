# Generated by Django 4.2.7 on 2024-01-15 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useraccount_user'),
        ('vaccine_campaign', '0005_remove_campaign_vaccines_offered_vaccine_campaign'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DoseBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_dose', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('first_dose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine_campaign.availabletime')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='accounts.useraccount')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_book', to='vaccine_campaign.vaccine')),
            ],
        ),
    ]
