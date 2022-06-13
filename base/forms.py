from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    # creates fields in the form acording to the Room class
    class Meta:
        model = Room
        fields = '__all__'
