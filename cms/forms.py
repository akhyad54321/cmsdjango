from django.forms import ModelForm
from .models import Company

class CmsForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'phone','address','city','state','country','industry_list']
