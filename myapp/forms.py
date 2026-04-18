from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

    def clean_skills(self):
        skills = self.cleaned_data.get('skills')
        if ',' not in skills:
            raise forms.ValidationError(
                "Enter at least 2 skills separated by commas (e.g. Python, Django)"
            )
        return skills