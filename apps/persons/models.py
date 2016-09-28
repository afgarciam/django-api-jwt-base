from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    
    # def __init__(self):
    #     return self.first_name + ' '+ self.last_name
