from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import (
    CharField,
    TextInput,
    EmailField,
    EmailInput,
    PasswordInput,
    JSONField,
    Textarea,
)
from .models import Event
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    username = CharField(
        max_length=50,
        min_length=3,
        required=True,
        widget=TextInput(attrs={"placeholder": "Username", "class": "form-control"}),
    )
    email = EmailField(
        required=True,
        widget=EmailInput(attrs={"placeholder": "Email", "class": "form-control"}),
    )
    password1 = PasswordInput(
        attrs={"placeholder": "Password", "class": "form-control"}
    )
    password2 = PasswordInput(
        attrs={"placeholder": "Confirm Password", "class": "form-control"}
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = CharField(
        max_length=50,
        min_length=3,
        required=True,
        widget=TextInput(attrs={"placeholder": "Username", "class": "form-control"}),
    )
    password = PasswordInput(attrs={"placeholder": "Password", "class": "form-control"})

    class Meta:
        model = User
        fields = ["username", "password"]


class EventForm(ModelForm):
    event_type = CharField(
        max_length=100,
        widget=TextInput(attrs={"placeholder": "Event Typre", "class": "form-control"}),
    )
    data = JSONField(
        widget=Textarea(
            attrs={"placeholder": "Event Data (JSON)", "class": "form-control"}
        )
    )

    class Meta:
        model = Event
        fields = ["event_type", "data"]
