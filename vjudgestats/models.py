from django.db import models

# Create your models here.


class VjudgeStandings(models.Model):
    contest_name=models.CharField(max_length=100)
    contest_details=models.TextField()
    

    def __str__(self):
        return self.contest_name
