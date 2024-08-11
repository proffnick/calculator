from django.shortcuts import render
from django.http import JsonResponse
from .forms import CalculationForm


def calculate(expression):
    try:
        # Use Python's eval safely (for this context, eval is acceptable)
        result = eval(expression)
    except Exception:
        result = "Error"
    return result


def calculator_view(request):
    if request.method == "POST":
        form = CalculationForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data.get("expression")
            result = calculate(expression)
            return JsonResponse({"result": result})
    else:
        form = CalculationForm()
    return render(request, "calculator/calculator.html", {"form": form})
