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
    

    