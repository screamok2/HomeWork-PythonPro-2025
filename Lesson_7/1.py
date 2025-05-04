import enum

class Role(enum.StrEnum):
    STUDENT = enum.auto()
    TEACHER = enum.auto()

class User:
    def __init__(self, name: str, email: str, role: Role) -> None:
        self.name = name
        self.email = email
        self.role = role


    def send_notification(self, notification):
        self.notification = notification

        print( f"From:{self.email}\n{notification.format()}\nRegards\n{self.name}\n\n")


class Notification:
    def __init__(self, subject: str, message: str, attachment: str = "") -> None:
        self.subject = subject
        self.message = message
        self.attachment = attachment  # Optional extra info

    def format(self) -> str:
        massage =f"Subject: {self.subject}\n---------------\nMessage: {self.message}"

        if self.attachment:
            massage += f"\nAttachment: {self.attachment}"
        return massage

        # TODO: implement basic notification formatting
        # TODO: think about `__str__` usage instead of `format`


class StudentNotification(Notification):
    def format(self) -> str:
        noti = super().format()
        return f"{noti}\nSent via Student Portal"
        # TODO: add "Sent via Student Portal" to the message


class TeacherNotification(Notification):
    def format(self) -> str:
        noti = super().format()
        return f"{noti}\nTeacher's Desk Notification"

        # TODO: add "Teacher's Desk Notification" to the message


def main():
    student_1 = User("Kolya", "kolya@gmail.com", Role.STUDENT)
    student_2 = User("Vasya", "vasya@gmail.com", Role.STUDENT)

    teacher_1 = User("math", "math@gmail.com", Role.TEACHER)

    message = input("Enter the subject and the massage with separator';' ")
    subject1, message1 = message.split(';')


    student_1_noti = StudentNotification ( subject=subject1, message=message1, attachment=None)

    student_2_noti = StudentNotification ("Wellcome", "Wellcome on the board ! ", "picture")
    teacher_1_noti = TeacherNotification ( "Hello", "How are you ? ")

    student_1.send_notification(student_1_noti)
    student_2.send_notification(student_2_noti)
    teacher_1.send_notification(teacher_1_noti)



if __name__ == "__main__":
    main()








