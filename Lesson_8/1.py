import time
import threading

students = {
    1 : {'name': 'Micky', 'marks':"1,1,1,1,1,1,1,1"},
    2 : {'name': 'john', 'marks':'2,2,2,2,2,2'},
    3 : {'name': 'Paul', 'marks':'4,4,4,4,4,4,4'},
    4 : {'name': 'Paul', 'marks':'5,5,5,5,5,5,5'},
    5 : {'name': 'Paul', 'marks':'3,3,3,3,3,3,3'},
    6 : {'name': 'Paul', 'marks':'3,2,3,4,3,4,3'},
    7 : {'name': 'Paul', 'marks':'1,3,1,3,3,3,4'},
    8 : {'name': 'Paul', 'marks':'3,3,3,3,3,3,3'},
    9 : {'name': 'Paul', 'marks':'1,3,1,3,3,3,4'},
    10 : {'name': 'Paul', 'marks':'3,3,3,3,3,3,3'},
    11: {'name': 'Paul', 'marks':'3,3,3,3,3,3,3'},
    12: {'name': 'Paul', 'marks':'3,3,3,3,3,3,3'},
    13: {'name': 'Paul', 'marks':'3,3,3,3,3,3,3'},

}
def total_number_students():
    return max(students.keys())



def average_mark ():
    marks = []
    time.sleep(4)  # simulation of calculation average mark for 100000 students
    for item in students:
        all_marks = list(map(int, students[item]["marks"].split(",")))
        marks.extend(all_marks)
        average_marks = round(sum(marks) / len(marks) , 2 )

    return average_marks

def input_marks():
    user_input = input("Enter marks:")
    print( f"Entered marks: {user_input}" )




def send_mail ():
    #time.sleep(2) # simulation of calculation average mark for 100000 students
    print( f"\nHello \ntotal number of students: {total_number_students()}\naverage mark : {average_mark()}")

thread1 = threading.Thread(target=send_mail)
thread2 = threading.Thread(target=input_marks)

thread1.start()
thread2.start()