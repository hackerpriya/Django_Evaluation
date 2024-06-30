# Payment_Management/views.py

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import ServiceUser, Services, Subscription

# Function-based views

def list_users(request):
    users = ServiceUser.objects.all()
    return render(request, 'list_users.html', {'users': users})

def user_details(request, user_id):
    user = get_object_or_404(ServiceUser, id=user_id)
    subscriptions = Subscription.objects.filter(user=user)
    return render(request, 'user_details.html', {'user': user, 'subscriptions': subscriptions})

def list_services(request):
    services = Services.objects.all()
    return render(request, 'list_services.html', {'services': services})

def service_details(request, type):
    service = get_object_or_404(Services, type=type)
    subscriptions = Subscription.objects.filter(service=service)
    return render(request, 'service_details.html', {'service': service, 'subscriptions': subscriptions})

def create_subscription_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        service_id = request.POST.get('service')
        amount = request.POST.get('amount')
        # Add logic to create subscription here
        return render(request, 'subscription_created.html')
    
    users = ServiceUser.objects.all()
    services = Services.objects.all()
    return render(request, 'create_subscription.html', {'users': users, 'services': services})


# Class-based views

class UserListView(ListView):
    model = ServiceUser
    template_name = 'list_users.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = ServiceUser
    template_name = 'user_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['subscriptions'] = Subscription.objects.filter(user=user)
        return context

class ServiceListView(ListView):
    model = Services
    template_name = 'list_services.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Services
    template_name = 'service_details.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        context['subscriptions'] = Subscription.objects.filter(service=service)
        return context

class CreateSubscriptionView(View):
    def get(self, request):
        users = ServiceUser.objects.all()
        services = Services.objects.all()
        return render(request, 'create_subscription.html', {'users': users, 'services': services})

    def post(self, request):
        user_id = request.POST.get('user')
        service_id = request.POST.get('service')
        amount = request.POST.get('amount')        
        return render(request, 'subscription_created.html')

