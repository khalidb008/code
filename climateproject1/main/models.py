from django.db import models

# Create your models here.
class climate(models.Model):
    location = models.CharField(max_length=50)
    temperature = models.FloatField()
    flood = models.FloatField()
    drought = models.FloatField(default=0)
    social_disruption = models.CharField(max_length=25)
    indigenous_forecasting = models.CharField(max_length=25)

    def __str__(self):
        return (f"Location: {self.location}, "
                f"Temperature: {self.temperature}, "
                f"Flood: {self.flood}, "
                f"Drought: {self.drought}, "
                f"Social Disruption: {self.social_disruption}, "
                f"Indigenous Forecasting: {self.indigenous_forecasting}")

class select_item(models.Model):
    item = models.ForeignKey(climate, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item     