from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import SimulationEntryUserForm, StrategyEntryUserForm
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Strategy simulator")


class UserFormView(FormView):
    template_name = "simulator/user_form.html"
    form_class = SimulationEntryUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["strategy_form"] = StrategyEntryUserForm()
        return context

    def form_valid(self, form):
        simulation_data = form.cleaned_data

        strategy_form = StrategyEntryUserForm(self.request.POST)
        if strategy_form.is_valid():
            strategy_data = strategy_form.cleaned_data
        else:
            strategy_data = None

        result = calculate_results(simulation_data, strategy_data)

        return render(self.request, "simulator/result.html", {"result": result})


def calculate_results(simulation_data, strategy_data):

    if simulation_data and strategy_data:
        initial_amount = simulation_data.get("initial_amount", 0)
        number_of_trades = simulation_data.get("number_of_trades", 0)
        accuracy = strategy_data.get("accuracy", 0)
        stop_loss = strategy_data.get("percentage_stop_loss", 0)
        take_profit = strategy_data.get("percentage_take_profit", 0)

        winning_trades = number_of_trades * accuracy
        losing_trades = number_of_trades - winning_trades

        result = initial_amount * (
            winning_trades * take_profit + losing_trades * stop_loss
        )

        return result


# Create your views here.
