from django import forms
from .models import Question, Option


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'description')
        labels = {
            'question': 'Question',
            'description': 'Description'
        }
        widgets = {
                   'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Question'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Question Description', 'rows':'3'}),
                } 


class OptionForm(forms.ModelForm):
  class Meta:
    model = Option
    fields = ["optionText"]
    labels = {
      'optionText':''
    }
    widgets = {
      'optionText': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Option'})
    }