from itertools import islice

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
    #   If you can really find the time, try to put this in excel and retrieve it from there through maybe Panda's python.
    questions_list = [['Vraag 1', ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']],
                      ['Vraag 2', ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']],
                      ['Vraag 3', ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']]]

    context = {'questions': questions_list}
    return render(request, 'questionslist/questionslist.html', context)

def processing_answers(request):
    data = request.POST

    # TODO: Points logic

    # Give the items an index number
    for element in enumerate(data.items()):
        # If the first element is the token, skip that element.
        if element[0] == 0:
            continue

        # Add remaining elements, which are the answers, to the database (file).
        question_number = element[1][0]
        input_answer = element[1][1]
        formatted_answer = f'Vraag {question_number}:\n\t{input_answer}\n'
        with open('results.txt', 'a') as f:
            f.write(formatted_answer)

    return HttpResponseRedirect('/resultaten/')
