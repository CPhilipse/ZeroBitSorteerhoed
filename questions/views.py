from django.http import HttpResponseRedirect
from django.shortcuts import render

''' TODO:
    3. From this function return a view that goes to the results page
        a. Pass the results as a variable (context variable) to the results page
            i. The results being: Points per specialisation and specialisation with the most points.
'''

def questionslist(request):
    # I think in PythonAnywhere you need the path /home/project/questions.txt or something like that.
    questions_list = []
    question_list_number = 0
    with open('questions.txt', 'r') as f:
        data = f.read()
        splitted_lines = data.split('\n')
        for index, element in enumerate(splitted_lines):
            if index % 2 == 0:
                questions = element.split('~')
                questions_list.append(questions)
            if index % 2 != 0:
                answers = element.split(';')
                questions_list[question_list_number].append(answers)
                question_list_number += 1

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
        # TODO: if answer is not acknowledigng the specialisation, then do NOT add +1.
        #   You can only do this if you have the answers ~_~
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
        points = f'BDaM punten: {BDaM_points}\nFICT punten: {FICT_points}\nIaT punten: {IaT_points}\nSE punten: {SE_points}\n'
        f.write(points)

    return HttpResponseRedirect('/resultaten/')
