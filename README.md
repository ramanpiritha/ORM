# Ex03 Django ORM Web Application
## Date: 11-09-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-09-11 100207.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import Bankloan,Bankloanadmin
admin.site.register(Bankloan,Bankloanadmin)

model.py    
    from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    Loanid=models.IntegerField(primary_key=True)
    Customername=models.CharField(max_length=50)
    Salary_slips=models.IntegerField()
    Accountno=models.IntegerField()
    Adharno=models.IntegerField()
    
    
class Bankloanadmin(admin.ModelAdmin):
    list_display=('Loanid','Customername','Salary_slips','Accountno','Adharno')
```
## OUTPUT
![alt text](<Screenshot (10).png>)
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
