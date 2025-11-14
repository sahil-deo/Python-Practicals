events = []

def addEvent(event):
    events.append(event)
    print("Event Added\n")

def processEvent():
    global events
    if len(events)==0:
        print("No Events in the list\n")
        return
    
    event = events[0]
    events = events[1:]
    print(f'Event Processed:{event}\n')

def removeEvent(event):
    if event in events:
        events.remove(event)
        print(f'Event Removed:{event}\n')
    else:
        print("Event not found\n")
def displayEvents():
    print(f'Events:{events}\n')


# start execution

while(True):
    option=input("1. Add an Event\n2. Process Event\n3. Cancel Event\n4. Show Pending Events\n5. Exit\n>")

    if option=="1":
        event=input("Event:")
        addEvent(event)

    elif option == "2":
        processEvent()
    elif option == "3":
        displayEvents()
        event = input("Enter Event to Cancel:")
        removeEvent(event)
    elif option == "4":
        displayEvents()
    elif option == "5":
        break
    else:
        print("Invalid Option...\n")



