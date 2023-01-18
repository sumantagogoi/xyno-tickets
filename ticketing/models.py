from django.db import models
import uuid

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True,null=True)
    email = models.CharField(max_length=50, blank=True,null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300, blank=True,null=True)
    notes = models.CharField(max_length=300, blank=True,null=True)


class Event(models.Model):
    client = models.ForeignKey(Client)  
    name = models.CharField(max_length=100)
    event_creative = models.ImageField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True,null=True)      
    status = models.BooleanField(default = True)


class Ticket (models.Model):
    event = models.ForeignKey(Event)   
    ticket_cat =  models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_tickets = models.IntegerField(blank=True,null=True)


class TSaleCounter(models.Model):
    ticket = models.ForeignKey(Ticket,unique=True)
    number_sold = models.IntegerField()


class Customer(models.Models):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True,null=True)
    address = models.CharField(max_length=100, blank=True,null=True)
    age = models.CharField(max_length=100, blank=True,null=True)


class TSoldData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket)
    customer =  models.ForeignKey(Customer)
    quantity = models.IntegerField(default = 1)
    txn_details = models.JSONField()
    status = models.CharField(choices=(("claimed", "claimed"),("booked", "booked"),("cancelled", "cancelled"),("refunded", "refunded")))

