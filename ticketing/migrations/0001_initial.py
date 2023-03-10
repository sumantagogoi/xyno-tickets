# Generated by Django 4.1.7 on 2023-02-28 17:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('notes', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('event_creative', models.ImageField(upload_to='')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ticketing.client')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_cat', models.CharField(max_length=100)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_tickets', models.IntegerField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ticketing.event')),
            ],
        ),
        migrations.CreateModel(
            name='TSoldData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('txn_details', models.JSONField()),
                ('status', models.CharField(choices=[('claimed', 'claimed'), ('booked', 'booked'), ('cancelled', 'cancelled'), ('refunded', 'refunded')], max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ticketing.customer')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ticketing.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TSaleCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_sold', models.IntegerField()),
                ('ticket', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='ticketing.ticket')),
            ],
        ),
    ]
