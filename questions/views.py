from django.http import HttpResponseRedirect
from django.shortcuts import render

from questions.forms import QuestionsForm

''' TODO:
    1. Make multiple inputs on the view.
        a. On submit, all this data will go to the function specified in the form component (see HTML forms).
    2. Then write the logic in that function and add it to a file.
    3. From this function return a view that goes to the results page
        a. Pass the results as a variable (context variable) to the results page
            i. The results being: Points per specialisation and specialisation with the most points.
'''

def questionslist(request):
    # TODO: perhaps retrieve the questions from a file.
    #      Perhaps put the answer options statically in the html file.
    questions_list = ['Hoe gaat het?', 'Alles goed?', 'Ben je oké?', 'Alles top?', 'Jij goed?', 'Sup?']
    answer_options = ['eens', 'oneens']

    context = {'questions': questions_list, 'answer_options': answer_options}
    return render(request, 'questionslist/questionslist.html', context)

def processing_answers(request):
    print('Request: ', request)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionsForm(request.POST)
        print('Form data: ', form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            context = {}

            return HttpResponseRedirect('/thanks/')
