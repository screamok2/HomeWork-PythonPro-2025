import csv
from pathlib import Path
# ─────────────────────────────────────────────────────────


STORAGE_FILE_NAME = Path(__file__).parent / "storage/students.csv"


# ─────────────────────────────────────────────────────────
# INFRASTRUCTURE
# ─────────────────────────────────────────────────────────

class Repository:
    """
    RAM: John, Marry, Mark
    SSD: John, Marry
    """
    def __init__(self):
        self.file = open(STORAGE_FILE_NAME, "r")
        self.students = self.get_storage()

        # close after reading
        self.file.close()


    def get_storage(self):
        with open(STORAGE_FILE_NAME, "r", encoding="utf-8", newline="") as file:
            self.file.seek(0)
            reader = csv.DictReader(self.file, fieldnames=["id", "name", "marks", "info"], delimiter=";")

            return list(reader)



    def add_student(self, student: dict):
        with open (STORAGE_FILE_NAME, mode="a", encoding="utf-8", newline="") as file:
            self.file = file

            self.students.append(student)
            writer = csv.DictWriter(self.file, fieldnames=["id", "name", "marks", "info"], delimiter=";")
            writer.writerow(student)


    def update_storage(self, students: list[dict]):
        with open(STORAGE_FILE_NAME, "w", encoding="utf-8", newline="\n") as file:
            writer = csv.DictWriter( file , fieldnames=["id", "name", "marks", "info"], delimiter=";")
            for student in students:
                writer.writerow(student)

        #file.close()



    # only the idea. we should perform writes only if we know user quit the application
    # better to create: `.save()` and call it on `quit` or any other command that is not covered
    # def __del__(self):
    #     self.file.seek(0)
    #     writer = csv.DictWriter(self.file, fieldnames=["id", "name", "marks", "info"])
    #     for student in self.students:
    #         writer.writerow(student)
    #
    #     self.file.close()


repo = Repository()

def inject_repository(func):
    def inner(*args, **kwargs):
        return func(*args, repo=repo, **kwargs)

    return inner



# ─────────────────────────────────────────────────────────
# DOMAIN (student, users, notification)
# ─────────────────────────────────────────────────────────
class StudentService:
    def __init__(self):
        self.repository = Repository()

    @inject_repository
    def add_student(self, student: dict) -> dict | None:
        self.student = student
        if len(student) != 2:
            return None

        if not student.get("name") or not student.get("marks"):
            return None
        else:
            # action

            #next_id = max(repo.students.keys())
            #repo[next_id] = student
            return student


    @inject_repository
    def show_students(self, repo: Repository):

        print("=========================\n")
        for student in repo.students:
            print(f"{student['id']}. Student {student['name']}\n")
        print("=========================\n")



    def show_student(self,student: dict) -> None:
        print(
            "=========================\n"
            f"Student {student['name']}\n"
            f"Marks: {student['marks']}\n"
            f"Info: {student['info']}\n"
            "=========================\n"
        )

    @inject_repository
    def delete_student(self, student_id: int, repo: Repository):

        students = [s for s in repo.students if int(s["id"]) != student_id]
        repo.update_storage(students)



    def update_student( id_: int, raw_input: str) -> dict | None:
        parsing_result = raw_input.split(";")
        if len(parsing_result) != 2:
            return None

        new_name, new_info = parsing_result

        student: dict | None = repo.students[int(id_)]

        if int(student["id"]) == id_:
            student["name"] = new_name
            student["info"] = new_info
            repo.update_storage(repo.students)
            return student

    @inject_repository
    def add_marks (self, idd: int, new_marks: str, repo: Repository):
        student = repo.students[int(idd)]
        if int(student["id"]) == idd:
            student["marks"] = student["marks"] + str(",") + new_marks
            repo.update_storage(repo.students)

            return student
# ─────────────────────────────────────────────────────────
# OPERATIONAL (APPLICATION) LAYER
# ─────────────────────────────────────────────────────────
def ask_student_payload() -> dict:
    ask_prompt = (
        "Enter student's payload data using text template: "
        "John Doe;1,2,3,4,5\n"
        "where 'John Doe' is a full name and [1,2,3,4,5] are marks.\n"
        "The data must be separated by ';'"
    )

    def parse(data) -> dict:
        name, raw_marks = data.split(";")
        new_id = int(repo.students[-1]["id"]) + 1
        return {

            "id": new_id,
            "name": name,
            "marks": raw_marks, #r[int(item) for item in raw_marks.replace(" ", "").split(",")],
            "info" : str()
        }

    user_data: str = input(ask_prompt)
    return parse(user_data)


def student_management_command_handle(command: str):
    students_service = StudentService()
    repo = Repository()
    if command == "show":
        students_service.show_students()

    elif command == "add":
         data = ask_student_payload()
         repo.add_student(data)

         if data is None:
            print("Error adding student")
         else:

            print(f"Student: {data["name"]} is added")

    elif command == "search":
        student_id = input("Enter student ID: ").strip()
        for student in repo.students:
            if student["id"] == student_id:
                students_service.show_student(student)
                return
        print(f"Student with ID {student_id} not found")


    elif command == "delete":

         student_id= int(input("\n Enter student's ID: "))
         students_service.delete_student(student_id)
         print(f"Student with ID {student_id} is deleted")

    elif command == "update":
         student_id: str = input("\nEnter student's ID: ")
         if not student_id:
             print("Student ID must be specified for update")
             return
         repo = Repository()
         id_ = int(student_id)
         student: dict | None = {}
         for item in repo.students:
             if item["id"] == student_id:
                 student = item

         if student is None:
             print(f"Student {student_id} not found")
             return

         students_service.show_student(student)
         print(
             f"\n\nTo update user's data, specify `name` and `info`, with `;` separator.\n"
         )

         user_input: str = input("Enter: ")
         updated_student: dict | None = StudentService.update_student(id_=id_, raw_input=user_input)

         if updated_student is None:
             print("Erorr on updating student")
         else:
             print(f"Student {updated_student['name']} is updated")

    elif command == "add mark":
        student_id = int(input("\nEnter student's ID: "))
        if not student_id:
            print("Student ID must be specified for update")
            return
        repo = Repository()
        idd = int(student_id)
        student: dict | None = {}
        for item in repo.students:
            if item["id"] == student_id:
                student = item
        if student is None:
            print(f"Student {student_id} not found")
            return


        #students_service.show_student(student)


        new_marks = input ("Enter marks with ',' separator  : ")

        updated_marks = students_service.add_marks(idd=idd, new_marks=new_marks)
        print(f"Student {updated_marks["name"]} marks added")
# ─────────────────────────────────────────────────────────
# PRESENTATION LAYER
# ─────────────────────────────────────────────────────────
def handle_user_input():
    OPERATIONAL_COMMANDS = ("quit", "help")
    STUDENT_MANAGEMENT_COMMANDS = ("show", "add", "search", "delete", "update", "add mark")
    AVAILABLE_COMMANDS = (*OPERATIONAL_COMMANDS, *STUDENT_MANAGEMENT_COMMANDS)

    HELP_MESSAGE = (
        "Hello in the Journal! User the menu to interact with the application.\n"
        f"Available commands: {AVAILABLE_COMMANDS}"
    )

    print(HELP_MESSAGE)

    while True:
        command = input("\n Select command: ")

        if command == "quit":
            print("\nThanks for using the Journal application")
            break
        elif command == "help":
            print(HELP_MESSAGE)
        else:
            student_management_command_handle(command)


# ─────────────────────────────────────────────────────────
# ENTRYPOINT
# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    handle_user_input()