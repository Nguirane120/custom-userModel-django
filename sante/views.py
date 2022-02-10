from django.shortcuts import render, redirect
from .forms import CustomerRegstrationn
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.





def registerCustomer(request):
    forms = CustomerRegstrationn()
    if request.method == "POST":
        forms = CustomerRegstrationn(request.POST)
        if forms.is_valid():
            forms.save()
            first_name = forms.cleaned_data.get('first_name')
            password = forms.cleaned_data.get('password1')
            account = authenticate(first_name=first_name, password=password)
            messages.success(request, "Account was created for " + first_name)
            login(request, account)
            return redirect('/home')
        else:
            forms = CustomerRegstrationn()
    context = {'forms':forms}
    return render(request, 'sante/register_client.html', context)



def loginCustomer(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            password = request.POST.get('password')

            user = authenticate(username=first_name, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                messages.info(request, 'firstname or passwor is incoorect')

        context = {}
        return render(request, 'sante/login_client.html', context)


def logOutUser(request):
    logout(request)
    return redirect('login-client')

def dashCleint(request):
    return render(request, "sante/dashboard_client.html", {})


def dashHospi(request):
    return render(request, "sante/dashboard_hospi.html", {})


def dashPharmaci(request):
    return render(request, "sante/dashboard_pharmaci.html", {})