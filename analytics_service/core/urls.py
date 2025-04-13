from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("auth/registration/", views.RegistrationView.as_view(), name="registration"),
    path(
        "auth/login/",
        LoginView.as_view(
            template_name="auth/login.html",
            form_class=LoginForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "auth/logout/",
        LogoutView.as_view(template_name="auth/logout.html"),
        name="logout",
    ),
    path("create_view/", views.EventFormView.as_view(), name="create_event"),
    path("event_list/", views.EventListView.as_view(), name="event_list"),
    path("event/<int:id>/", views.EventDetailView.as_view(), name="event_detail"),
]
