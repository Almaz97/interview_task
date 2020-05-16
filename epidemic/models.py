from django.db import models


class Country(models.Model):
    class Meta:
        db_table = 'country'

    name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class DailyInfectionScan(models.Model):
    class Meta:
        db_table = 'daily_infection_scan'

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    infected = models.IntegerField()
    died = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.date)