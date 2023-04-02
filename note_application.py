
def grade_note_average(line):
    line = line[:-1] #aradaki boşluklar silinir.
    list = line.split(':')

    studentName = list[0]
    notes = list[1].split(',')

    note1 = float(notes[0])
    note2 = float(notes[1])
    note3 = float(notes[2])

    average = (note1 + note2 + note3)/3

    if average >= 90 and average <= 100:
        character = 'AA'
    elif average >= 85 and average <= 89:
        character = 'BA'
    elif average >= 80 and average <= 84:
        character = 'BB'
    elif average >= 75 and average <= 79:
        character = 'CB'
    else:
        character = 'FF'
    return studentName + ':' + character + "\n"
def read_notes():
    with open("exam_notes.txt", 'r', encoding= 'utf-8') as file:
        for line in file:
            print(grade_note_average(line)) 
def input_note():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    note1 = input("Enter note: ")
    note2 = input("Enter note: ")
    note3 = input("Enter note: ")
    with open("exam_notes.txt", 'a', encoding='utf-8') as file:   
        file.write(name + ' ' + surname + ':' + note1 + ',' + note2 + ',' + note3 +'\n')

def save_notes():
    with open("exam_notes.txt", 'r', encoding='utf-8') as file: 
        list = [] 

        for i in file:
            list.append(grade_note_average(i))
        with open("exam_notes.txt", 'w', encoding='utf-8') as file2: 
            for i in list:
                file2.write(i)

while True:
    process = input('1. Read Notes\n2. Input note\n3. Save notes\n4. Exit\nEnter a number: ')
    if process == '1':
        read_notes()
    elif process == '2':
        input_note()
    elif process == '3':
        save_notes()
    else:
        break