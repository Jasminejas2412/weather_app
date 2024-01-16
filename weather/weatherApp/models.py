from django.db import models 


class weather(models.Model):
    city=models.CharField(max_length=50,default="")
    weather=models.CharField(max_length=59)
    pressure=models.CharField(max_length=60)
    kelvin_temperature=models.IntegerField(default="",null=True)
    humidity=models.CharField(max_length=60)
    celsius_temperature=models.IntegerField(default="",null=True)




def __str__(self):
    return self.kelvin_temperature,self.celsius_temperature

