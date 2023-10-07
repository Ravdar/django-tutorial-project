from django import forms
from .models import SimulationEntryData, StrategyEntryData


class SimulationEntryUserForm(forms.ModelForm):
    class Meta:
        model = SimulationEntryData
        fields = ["initial_amount", "number_of_simulations", "number_of_trades"]


class StrategyEntryUserForm(forms.ModelForm):
    class Meta:
        model = StrategyEntryData
        fields = ["percentage_stop_loss", "percentage_take_profit", "accuracy"]

