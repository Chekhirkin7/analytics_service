from django.shortcuts import render, redirect
from .forms import RegistrationForm, EventForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event
from .tasks import process_event


class RegistrationView(View):
    template_name = "auth/registration.html"
    form_class = RegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:index")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="core:login")
        return render(request, self.template_name, {"form": form})


class EventFormView(LoginRequiredMixin, View):
    login_url = "auth/registration"
    template_name = "event/create_event.html"
    form_class = EventForm

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            process_event.delay(form.instance.id)
            return redirect(to="core:event_list")
        return render(request, self.template_name, {"form": form})


class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class EventListView(LoginRequiredMixin, View):
    login_url = "auth/registration"
    template_name = "event/show_event.html"

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        return render(request, self.template_name, {"events": events})


class EventDetailView(LoginRequiredMixin, View):
    login_url = "auth/registration"
    template_name = "event/event_detail.html"

    def get(self, request, id):
        event = Event.objects.get(id=id)
        return render(request, self.template_name, {"event": event})
