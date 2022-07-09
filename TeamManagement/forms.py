from django import forms
from .models import TeamMember


# https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#modelform
class TeamMemberForm(forms.ModelForm):

    class Meta:
        model = TeamMember
        widgets = {'role': forms.RadioSelect()}
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
