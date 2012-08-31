from django import forms

from django_select2 import *

from .models import Employee, Dept, ClassRoom, Lab

class EmployeeChoices(AutoModelSelect2Field):
    queryset = Employee.objects
    search_fields = ['name__icontains', ]

class ClassRoomChoices(AutoModelSelect2MultipleField):
    queryset = ClassRoom.objects
    search_fields = ['number__icontains', ]

class ClassRoomSingleChoices(AutoModelSelect2Field):
    queryset = ClassRoom.objects
    search_fields = ['number__icontains', ]

class EmployeeForm(forms.ModelForm):
    manager = EmployeeChoices(required=False)
    dept = ModelSelect2Field(queryset=Dept.objects)
    
    class Meta:
        model = Employee

class DeptForm(forms.ModelForm):
    allotted_rooms = ClassRoomChoices()
    allotted_labs = ModelSelect2MultipleField(queryset=Lab.objects, required=False)

    class Meta:
        model = Dept

class MixedForm(forms.Form):
    emp1 = EmployeeChoices()
    rooms1 = ClassRoomChoices()
    emp2 = EmployeeChoices()
    rooms2 = ClassRoomChoices()
    rooms3 = ClassRoomSingleChoices()

# These are just for testing Auto registration of fields
EmployeeChoices() # Should already be registered
EmployeeChoices(auto_id="EmployeeChoices_CustomAutoId") # Should get registered

class InitialValueForm(forms.Form):
    select2Choice = Select2ChoiceField(initial=2, choices=((1, "First"), (2, "Second"), (3, "Third"), ))
    select2MultipleChoice = Select2MultipleChoiceField(initial=[2,3], choices=((1, "First"), (2, "Second"), (3, "Third"), ))
    heavySelect2Choice = AutoSelect2Field(initial=2, choices=((1, "First"), (2, "Second"), (3, "Third"), ))
    heavySelect2MultipleChoice = AutoSelect2MultipleField(initial=[1,3], choices=((1, "First"), (2, "Second"), (3, "Third"), ))
