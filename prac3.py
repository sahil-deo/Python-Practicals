document = ""

undo_stack = []
redo_stack = []

def change(newstate):
    global document
    global undo_stack
    undo_stack.append(document)
    document=newstate

    print(f'\nDocument:{document}\n')

def undo():
    global document
    global redo_stack
    global undo_stack
    if len(undo_stack)==0:
        print("undo stack is empty")
        return

    redo_stack.append(document)
    document=undo_stack.pop()
    print(f'\nDocument:{document}\n')

def redo():
    global redo_stack
    global undo_stack
    global document
    if len(redo_stack)==0:
        print("redo stack is empty")
        return
    
    undo_stack.append(document)
    document=redo_stack.pop()
    print(f'\nDocument:{document}\n')

# start execution

while(True):
    option=input("1. Status\n2. Change\n3. Undo\n4. Redo\n5. Exit\n>")
    if option == "1":
        print(document)
        print("Undo Stack:", undo_stack)
        print("Redo Stack:", redo_stack)

    elif option == "2":
        newstate=input("New Change:")
        change(newstate)
    elif option == "3":
        undo()
    elif option == "4":
        redo()
    elif option == "5":
        break
    else:
        print("Invalid Option try again...\n")
