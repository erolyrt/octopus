from django import forms
from matplotlib.pyplot import cla
from .models import Csv

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)