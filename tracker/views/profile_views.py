from django.shortcuts import render, redirect
from tracker.forms import ProfileForm
from tracker.models import Profile, Expense


# Create your views here.


def home_page_view(request):
    if Profile.objects.all():
        all_expenses = Expense.objects.all()
        profile = Profile.objects.all()[0]
        context = {
            "budget_left": profile.budget - sum([exp.price for exp in all_expenses]),
            "profile": profile,
            "all_expenses": all_expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.POST:
            form = ProfileForm(request.POST)
            print(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
        else:
            context = {
                "form": ProfileForm(),
            }
            return render(request, 'home-no-profile.html', context)


def profile_view(request):
    profile = Profile.objects.all()[0]
    context = {
       "profile": profile
    }
    return render(request, 'profile.html', context)


def edit_profile_view(request):
    profile = Profile.objects.all()[0]
    context = {
        "form": ProfileForm(instance=profile)
    }
    if request.POST:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(request, 'profile-edit.html', context)

    return render(request, 'profile-edit.html', context)


def delete_profile_view(request):
    profile = Profile.objects.all()[0]
    all_expenses = Expense.objects.all()
    if request.POST:
        all_expenses.delete()
        profile.delete()
        return redirect('home page')
    return render(request, 'profile-delete.html')
