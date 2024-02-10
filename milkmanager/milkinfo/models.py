from django.db import models


class Cistern(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    volume = models.IntegerField(default=300)
    current_volume = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FillHistory(models.Model):
    cistern = models.ForeignKey(Cistern, on_delete=models.CASCADE)
    filler_name = models.CharField(max_length=100)
    filled_volume = models.IntegerField()
    filled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.filler_name} - {self.filled_volume}L - {self.cistern.name}"
