from django import forms
from .models import User
#from SpecialistAPI.models import Specialist


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'start_reception', 'finish_reception', 'date', )
        #fields = ('full_name',)
        #fields = '__all__'

    def get_object(self):
        return User

