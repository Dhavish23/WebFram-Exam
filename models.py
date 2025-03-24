from django.db import models  

# This is the Salesperson model whihch will it stores info about salespeople
class Salesperson(models.Model):
    id = models.AutoField(primary_key=True)  
    last_name = models.CharField(max_length=100)  
    first_name = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  

# Customer model  for storing customer details
class Customer(models.Model):
    id = models.AutoField(primary_key=True)  
    last_name = models.CharField(max_length=100)  
    first_name = models.CharField(max_length=100)  
    phone_number = models.CharField(max_length=20, unique=True)  
    address = models.TextField()  
    city = models.CharField(max_length=100)  
    state_province = models.CharField(max_length=100)  
    country = models.CharField(max_length=100)  
    postal_code = models.CharField(max_length=20)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  

# Car model for storing car details
class Car(models.Model):
    id = models.AutoField(primary_key=True)  
    serial_number = models.CharField(max_length=50, unique=True)  
    make = models.CharField(max_length=100) 
    model = models.CharField(max_length=100)  
    colour = models.CharField(max_length=50)  
    year = models.PositiveIntegerField()  
    is_for_sale = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"  

# SalesInvoice model for storing sales invoice details
class SalesInvoice(models.Model):
    id = models.AutoField(primary_key=True)  
    invoice_number = models.CharField(max_length=50, unique=True)  
    date = models.DateField(auto_now_add=True)  
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)  

# Mechanic model for storing mechanic details
class Mechanic(models.Model):
    id = models.AutoField(primary_key=True)  
    last_name = models.CharField(max_length=100)  
    first_name = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 

# ServiceTicket model for storing service ticket details
class ServiceTicket(models.Model):
    id = models.AutoField(primary_key=True)  
    service_ticket_number = models.CharField(max_length=50, unique=True)  
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    date_received = models.DateField(auto_now_add=True)  
    comments = models.TextField(blank=True) 
    date_returned = models.DateField(null=True, blank=True)  

# Service model for storing service details
class Service(models.Model):
    id = models.AutoField(primary_key=True)  
    service_name = models.CharField(max_length=100)  
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2)  

# ServiceMechanic model for linking services, mechanics, and tickets
class ServiceMechanic(models.Model):
    id = models.AutoField(primary_key=True)  
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)  
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)  
    hours = models.DecimalField(max_digits=5, decimal_places=2) 
    comment = models.TextField(blank=True)  
    rate = models.DecimalField(max_digits=10, decimal_places=2) 

# Part model for storing part details
class Part(models.Model):
    id = models.AutoField(primary_key=True)  
    part_number = models.CharField(max_length=50, unique=True)  
    description = models.TextField()  
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2) 
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)  

# PartsUsed model for linking parts to service tickets
class PartsUsed(models.Model):
    id = models.AutoField(primary_key=True)  
    part = models.ForeignKey(Part, on_delete=models.CASCADE) 
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)  
    number_used = models.PositiveIntegerField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
