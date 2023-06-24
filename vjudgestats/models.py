from django.db import models

# Create your models here.


class recentStandings(models.Model):
    team_name=models.CharField(max_length=100)
    rank=models.IntegerField()
    score=models.IntegerField()
    penalty=models.IntegerField()
    

    def __str__(self):
        return self.team_name
