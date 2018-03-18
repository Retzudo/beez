from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'