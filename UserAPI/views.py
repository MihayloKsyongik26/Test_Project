from django.shortcuts import render, redirect, reverse
from SpecialistAPI.models import Specialist
from django.http import HttpResponse
from .forms import RegisterForm
from .models import User
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView


def index(request):
    search_location = request.GET.get('search_location', '')
    search_worker = request.GET.get('search_worker', '')
    if search_location and not(search_worker):
        specs = Specialist.objects.filter(location=search_location)
    elif search_worker and not(search_location):
        specs = Specialist.objects.filter(worker = search_worker)
    elif search_location and search_worker:
        specs = Specialist.objects.filter(location=search_location, worker = search_worker)
    else:
        specs = Specialist.objects.all()


    return render(request, 'SpecialistAPI/index.html', {'specs': specs})


class Register(FormMixin, DetailView):
    model = Specialist
    template_name = 'SpecialistAPI/register.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            k = form.get_object().full_name
            print(k)
            return self.form_valid(form)
        else:
            return self.form_valid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.specialist = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')