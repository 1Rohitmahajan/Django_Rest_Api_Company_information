from django.db import models

# Create your models here.

#Creating Comany Model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField(max_length=300)
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Pharmacist','pharmacist'),("No IT","No IT"),("Agriculture","Agriculture")))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50,unique=True)  
    email=models.CharField(max_length=50,null=False,blank=False)  
    address=models.CharField(max_length=100,blank=False)      
    phone=models.CharField(max_length=50,blank=False)
    about=models.TextField(max_length=300)
    position=models.CharField(max_length=50,choices=(('Manager','manager'),('Human Resource','HR'),('Project Leader','pl'),('Software Developer','sd'),('Fronted Developer','fd'),('Backend Developer','bd')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE) #one to many relationship
    def __str__(self):
        return self.name