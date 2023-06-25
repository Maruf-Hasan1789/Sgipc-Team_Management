from django.db import models

# Create your models here.


#this models store the vjudge standings.Here the contest details is added as json
#file later the database will be updated...

class VjudgeStandings(models.Model):
    contest_name=models.CharField(max_length=100)
    contest_details=models.TextField()
    

    def __str__(self):
        return self.contest_name
