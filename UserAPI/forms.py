from django import forms
from .models import User
#from SpecialistAPI.models import Specialist


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'start_reception', 'finish_reception', 'date', )

    def get_object(self):
        return User

