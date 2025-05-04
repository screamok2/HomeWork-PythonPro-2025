class User:
    username: str
    password: str
users = { 'Alice':"1111",
          'Michael':"2222",
          'Emily':"3333",
          'James':"4444"
         }


def auth (*args):
    name = input("Enter the username: ")
    password = input( " Enter the password: ")
    if name in users.keys():
        while password != users[name]:
            print("INCORRECT PASSWORD")
            password = input("enter correct password: ")
        else:
            print(f"Hello {name} ")


@auth
def command(payload):
    print(f"Executing command by authorized user.\nPayload: {payload}")

while user_input := input("Enter anything: "):
    command(user_input)