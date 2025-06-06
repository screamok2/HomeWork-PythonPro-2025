# ─────────────────────────────────────────────────────────
# STORAGE SIMULATION
# ─────────────────────────────────────────────────────────
from tkinter.font import names

storage: dict[int, dict] = {
    1: {
        "name": "Alice Johnson",
        "marks": [7, 8, 9, 10, 6, 7, 8],
        "info": "Alice Johnson is 18 y.o. Interests: math",
    },
    2: {
        "name": "Michael Smith",
        "marks": [6, 5, 7, 8, 7, 9, 10],
        "info": "Michael Smith is 19 y.o. Interests: science",
    },
    3: {
        "name": "Emily Davis",
        "marks": [9, 8, 8, 7, 6, 7, 7],
        "info": "Emily Davis is 17 y.o. Interests: literature",
    },
    4: {
        "name": "James Wilson",
        "marks": [5, 6, 7, 8, 9, 10, 11],
        "info": "James Wilson is 20 y.o. Interests: sports",
    },
    5: {
        "name": "Olivia Martinez",
        "marks": [10, 9, 8, 7, 6, 5, 4],
        "info": "Olivia Martinez is 18 y.o. Interests: art",
    },
    6: {
        "name": "Emily Davis",
        "marks": [4, 5, 6, 7, 8, 9, 10],
        "info": "Daniel Brown is 19 y.o. Interests: music",
    },
    7: {
        "name": "Sophia Taylor",
        "marks": [11, 10, 9, 8, 7, 6, 5],
        "info": "Sophia Taylor is 20 y.o. Interests: physics",
    },
    8: {
        "name": "William Anderson",
        "marks": [7, 7, 7, 7, 7, 7, 7],
        "info": "William Anderson is 18 y.o. Interests: chemistry",
    },
    9: {
        "name": "Isabella Thomas",
        "marks": [8, 8, 8, 8, 8, 8, 8],
        "info": "Isabella Thomas is 19 y.o. Interests: biology",
    },
    10: {
        "name": "Benjamin Jackson",
        "marks": [9, 9, 9, 9, 9, 9, 9],
        "info": "Benjamin Jackson is 20 y.o. Interests: history",
    },
}


# ─────────────────────────────────────────────────────────
# CRUD
# ─────────────────────────────────────────────────────────
def add_student(student: dict) -> dict | None:
    if len(student) <= 2:
        return None

    if not student.get("name") or not student.get("marks"):
        return None
    else:
        # action
        next_id = max(storage.keys())+1
        storage[next_id] = student
        return student


def show_students():
    print("=========================\n")
    for id_, student in storage.items():
        print(f"{id_}. Student {student['name']}\n")
    print("=========================\n")


def show_student(student: dict) -> None:
    print(
        "=========================\n"
        f"Student {student['name']}\n"
        f"Marks: {student['marks']}\n"
        f"Info: {student['info']}\n"
        "=========================\n"
    )


def update_student(id_: int, raw_input: str) -> dict | None:
    if raw_input == "name":
        new_name = input("Enter new name: ")
        storage.get(id_)["name"] = new_name

    elif raw_input == "info":
        new_info = input("Enter new info: ")
        if new_info == str():
            storage.get(id_)["info"] = str()
        if new_info not in storage.get(id_)["info"] :
            storage.get(id_)["info"] = storage.get(id_)["info"] +","+ new_info
        elif new_info in storage.get(id_)["info"]:
            storage.get(id_)["info"] = new_info

    elif raw_input == "marks":
        new_marks = input("Enter new marks with separator ',': ")
        new_marks1 = [int(item) for item in new_marks.replace(" ", "").split(",")]
        storage.get(id_)["marks"] = new_marks1




# ─────────────────────────────────────────────────────────
# OPERATIONAL LAYER
# ─────────────────────────────────────────────────────────
def ask_student_payload() -> dict:
    ask_prompt = (
        "Enter student's payload data using text template: "
        "John Doe;1,2,3,4,5 ; info\n"
        "where 'John Doe' is a full name and [1,2,3,4,5] are marks.\n"
        "The data must be separated by ';'"
    )

    def parse(data) -> dict:
       # name, raw_marks , info = data.split(";")
        st_data = data.split(";")
        if len(st_data) == 2:
            name, raw_marks = st_data
            info =str()
        elif len(st_data) == 3:
            name, raw_marks, info = st_data
        return {
            "name": name,
            "marks": [int(item) for item in raw_marks.replace(" ", "").split(",")],
            "info": info
        }

    user_data: str = input(ask_prompt)
    return parse(user_data)


def student_management_command_handle(command: str):
    if command == "show":
        show_students()
    elif command == "add":
        data = ask_student_payload()
        if data:
            student: dict | None = add_student(data)
            if student is None:
                print("Error adding student")
            else:
                print(f"Student: {student['name']} is added")
        else:
            print("The student's data is NOT correct. Please try again")
    elif command == "search":
        student_id: str = input("\nEnter student's ID: ")
        if not student_id:
            print("Student's ID is required to search")
            return

        student: dict | None = storage.get(int(student_id))
        if student is None:
            print("Error adding student")
        else:
            show_student(student)
            print(f"Student {student_id} not found")
    elif command == "delete":
        student_id: str = input("\nEnter student's ID: ")
        if not student_id:
            print("Student's id is required to delete")
            return

        id_ = int(student_id)
        if storage.get(id_):
            print(f"Student {storage.get(id_)["name"] }is deleted")
            del storage[id_]

    elif command == "update":
        student_id: str = input("\nEnter student's ID: ")
        if not student_id:
            print("Student ID must be specified for update")
            return

        id_ = int(student_id)
        student: dict | None = storage.get(id_)
        if student is None:
            print(f"Student {student_id} not found")
            return

        show_student(student)
        print(
            f"\n\nTo update user's data, specify `name`, `info`, 'marks' "
        )

        user_input: str = input("Enter: ")
        updated_student: dict | None = update_student(id_=id_, raw_input=user_input)

        if updated_student is None:
            print("Erorr on updating student")
        else:
            print(f"Student {updated_student['name']} is updated")
        show_student(student)

def handle_user_input():
    OPERATIONAL_COMMANDS = ("quit", "help")
    STUDENT_MANAGEMENT_COMMANDS = ("show", "add", "search", "delete", "update")
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