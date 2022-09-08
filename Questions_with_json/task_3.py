import json
import os
from datetime import datetime

# with open('works.json', 'r') as file:
#     person = json.load(file)
#     print(person['response']['items'])
#     for item in person['response']['items']:
#         print(item['first_name'], item['last_name'])
#         del item['id']
#         item['like'] = randint(100, 300)
#     with open('new_work.json', 'w') as like:
#         json.dump(person, like, indent=4, sort_keys=True)


data = {}
with open('data.json', 'r') as file:
    task = json.load(file)
    # print(task['exam_content'])
    exam_cont = task['exam_content']
    for i in exam_cont.keys():
        print(i)
        dct = ['question', 'a', 'b', 'c', 'd']

        for j in dct:
            print(f'{j} : {exam_cont[i].get(j)}')
        answer = input('Enter Answer: ')
        for k in dct:
            print(f'{k} : {exam_cont[i].get(k)}')
            if answer == k:
                selected_answer = f'{answer} : {exam_cont[i].get(k)}'
                data[i] = selected_answer

                print(selected_answer)

    with open('answer.json', 'w') as like:
        json.dump(data, like, indent=4)


