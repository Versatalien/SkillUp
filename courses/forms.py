from django import forms 
from django.forms.models import inlineformset_factory
from .models import Courses,Module 

ModuleFormSet = inlineformset_factory(Courses, 
                                      Module,
                                      fields=['title','description'],
                                      extra=2, 
                                      can_delete=True
    
                                    )