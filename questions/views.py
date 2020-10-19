from django.http import HttpResponseRedirect
from django.shortcuts import render

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
    questions_list = [['BDaM', 'Ben jij geïnteresseerd in het automatiseren van bepaalde processen?',
                       ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']],
                      ['BDaM SE', 'Wil jij graag leren hoe je data efficiënt opslaat in een database?',
                       ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']],
                      ['BDaM', 'Is analyseren van data iets wat jou aanspreekt?',
                       ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']],
                      ['BDaM FICT', 'Wil jij leren onderzoek te doen naar bepaalde data om jou gestelde bewering te kunnen onderbouwen?',
                       ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']],
                      ['BDaM', 'Wil jij doormiddel van opgeslagen data voorspellingen kunnen doen over toekomstige ontwikkelingen? ',
                       ['antwoord 1', 'antwoord 2', 'antwoord 3', 'antwoord 4']]]

    context = {'questions': questions_list}
    return render(request, 'questionslist/questionslist.html', context)

def processing_answers(request):
    data = request.POST

    BDaM_points = 0
    FICT_points = 0
    IaT_points = 0
    SE_points = 0
    # Give the items an index number
    for element in enumerate(data.items()):
        # If the first element is the token, skip that element.
        if element[0] == 0:
            continue

        # Points logic
        # TODO: if answer is not acknowledigng the specialisation, then do NOT add +1
        if 'BDaM' in element[1][0]:
            BDaM_points += 1
        if 'FICT' in element[1][0]:
            FICT_points += 1
        if 'IaT' in element[1][0]:
            IaT_points += 1
        if 'SE' in element[1][0]:
            SE_points += 1

        # Add remaining elements, which are the answers, to the database (file).
        question_number = element[1][0]
        input_answer = element[1][1]
        formatted_answer = f'Vraag {question_number}:\n\t{input_answer}\n'
        with open('results.txt', 'a') as f:
            f.write(formatted_answer)

    with open('results.txt', 'a') as f:
        points = f'BDaM punten: {BDaM_points}\nFICT punten: {FICT_points}\nIaT punten: {IaT_points}\nSE punten: {SE_points}'
        f.write(points)

    return HttpResponseRedirect('/resultaten/')
