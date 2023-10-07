from django.db import models


class SimulationEntryData(models.Model):
    initial_amount = models.IntegerField()
    number_of_simulations = models.IntegerField()
    number_of_trades = models.IntegerField()


class StrategyEntryData(models.Model):
    percentage_stop_loss = models.FloatField()
    percentage_take_profit = models.FloatField()
    accuracy = models.FloatField()
    # Add more things here after testing out this simple model
