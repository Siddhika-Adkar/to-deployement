from django.db import models

# Create your models here.
class Register(models.Model):
    rname=models.CharField(max_length=30)
    rmail=models.EmailField()
    rpass=models.CharField(max_length=10)
    rrpass=models.CharField(max_length=10)
    #rphn:models.IntegerField(max_length=10)

#   def __str__(self):
#       return self.enameclass40
