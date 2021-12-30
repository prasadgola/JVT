from django import forms
from onemoreapp.models import Person



class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = "__all__"