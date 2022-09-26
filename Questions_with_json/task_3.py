import json



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


