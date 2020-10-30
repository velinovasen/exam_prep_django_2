from django.shortcuts import render, redirect
from tracker.forms import ExpenseForm, DisabledExpenseForm
from tracker.models import Expense

# Create your views here.


def create_expense_view(request):
    if request.POST:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        "form": ExpenseForm()
    }
    return render(request, 'expense-create.html', context)


def edit_expense_view(request, my_id):
    exp = Expense.objects.get(pk=my_id)
    if request.POST:
        form = ExpenseForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        "form": ExpenseForm(instance=exp)
        }
    return render(request, 'expense-edit.html', context)


def delete_expense_view(request, my_id):
    exp = Expense.objects.get(pk=my_id)
    if request.POST:
        exp.delete()
        return redirect('home page')
    context = {
        "form": DisabledExpenseForm(instance=exp)
    }
    return render(request, 'expense-delete.html', context)
