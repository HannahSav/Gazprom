import DBlogic


def ask(connection):
    print("\nWhat do u wanna?\n"
          "1.I wanna to find article by the title.\n"
          "2.Read a joke.")
    choice = input()
    if int(choice) == 1:
        print("Print title, pls")
        title = input()
        print("What format do u want?\n"
              "1. Just one string.\n"
              "2. Perfect json.")
        format = input()
        find_by_title(connection, title, format)
    else:
        print("Что будет если ворону ударит током?\n\n press anything")
        input()
        print("Электро CAR\n")


def find_by_title(connection, title, format):
    article = DBlogic.ask_by_title(connection, title)
