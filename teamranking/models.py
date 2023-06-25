from django.db import models

# Create your models here.



#this model store the information about the current team standings

class teamInformation(models.Model):
    team_name=models.CharField(max_length=200)
    rating=models.IntegerField(default=1500)
    hidden_rating=models.IntegerField(default=1500)
    attended_contests=models.IntegerField(default=0)
    rating_change=models.IntegerField(default=0)
    def __str__(self):
        return self.team_name