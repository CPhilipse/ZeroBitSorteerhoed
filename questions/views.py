import uuid
from django.http import HttpResponseRedirect
from django.shortcuts import render

''' TODO:
    3. From this function return a view that goes to the results page
        a. Pass the results as a variable (context variable) to the results page
            i. The results being: Points per specialisation and specialisation with the most points.
'''

# def questionslist(request, username):
def questionslist(request):
    # I think in PythonAnywhere you need the path /home/project/questions.txt or something like that.
    questions_list = []
    question_list_number = 0
    with open('questions.txt', 'r') as f:
        data = f.read()
        splitted_lines = data.split('\n')
        for index, element in enumerate(splitted_lines):
            if index % 2 == 0:
                # Text before ~ is the id of the question.
                questions = element.split('~')
                questions_list.append(questions)
            if index % 2 != 0:
                # The ; is to separate the answers in the file
                answers = element.split(';')
                questions_list[question_list_number].append(answers)
                question_list_number += 1

    # Remove empty question from list.
    questions_list.remove([''])

    test_username = 'test_usernameHAI'
    context = {'questions': questions_list, 'username': test_username}
    return render(request, 'questionslist/questionslist.html', context)

# If user hasn't entered an username, create an unique username
no_username_backup_id = uuid.uuid4()
def processing_answers(request, username=no_username_backup_id):
    data = request.POST

    # Create file for each new user. Does user already have a record? Update his record.
    with open(f'results/results{username}.txt', 'w') as f:
        pass

    BDaM_points = 0
    FICT_points = 0
    IaT_points = 0
    SE_points = 0
    # Give the items an index number
    for element in enumerate(data.items()):
        # If the first element is the token, skip that element.
        if element[0] == 0:
            continue

        ''' Points logic '''
        # After each answer that should give points there is an 1 added in the questions file.
        # With this manner we can recognize the answer that should give a point.
        # If answer_id is equal to 1, then add points else just don't
        answer_id = element[1][1][-1]
        if 'BDaM' in element[1][0]:
            if answer_id == '1':
                BDaM_points += 1
        if 'FICT' in element[1][0]:
            if answer_id == '1':
                FICT_points += 1
        if 'IaT' in element[1][0]:
            if answer_id == '1':
                IaT_points += 1
        if 'SE' in element[1][0]:
            if answer_id == '1':
                SE_points += 1

        # Add remaining elements, which are the answers, to the database (file).
        question_number = element[1][0]
        input_answer = element[1][1]
        formatted_answer = f'Vraag {question_number}:\n\t{input_answer}\n'
        with open(f'results/results{username}.txt', 'a') as f:
            f.write(formatted_answer)

    with open(f'results/results{username}.txt', 'a') as f:
        points = f'BDaM punten: {BDaM_points}\nFICT punten: {FICT_points}\nIaT punten: {IaT_points}\nSE punten: {SE_points}\n'
        f.write(points)

    return HttpResponseRedirect(f'/resultaten/{username}/')
