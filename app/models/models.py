from django.db import models


class Match(models.Model):

    #matchId = models.IntegerField()
    address = models.CharField(max_length=100)

    class Meta:db_table = 'match'



