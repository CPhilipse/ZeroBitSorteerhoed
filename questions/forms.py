from django import forms

class QuestionsForm(forms.Form):
    for i in range(1, 21):
        print('Loop: ', i)
        question = forms.CharField(label=f'vraag{i}', max_length=20)
        answer = forms.CharField(label=f'antwoord{i}', max_length=20)
