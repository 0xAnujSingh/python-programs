class TodoItem:
    def __init__(self, msg):
        self.msg = msg
        self.done = False

    def complete(self):
        self.done = True

class TodoList:
    def add(self, msg):
        item = TodoItem(msg)
        items.append(item)

        print("item added")

    def display(self):
        index = 0
        for i in items:
          print(index, i.done, i.msg)
          index += 1

    def done(self, idx):
        try:
            item = items[idx]
            item.complete()
            print("Item marked as Done!")
        except IndexError:
            print("Index not found")

    def undo(self, idx):
        try:
            item = items[idx]
            item.done = False
            print("Item marked as Not Done!")
        except IndexError:
            print("Index not found")

    def flush(self):
        items.clear()
        print("flush")

## Interface
print("ToDo Application Commands List\n")
print("add: To add new item")
print("list: To display all items")
print("done: To mark an item as done")
print("flush: To flush the list")
print("exit: To close the application\n")

lists = {
    'task': TodoList()
}

activeList = lists['task']

while True:
    cmd = input("Enter A Command: ")

    if cmd == "new":
        name = input("List Name")

        if (lists[name]):
            print('List already exists')
            continue

        lists[name] = TodoList(name)

    elif cmd == "change":
        list = input("Which List?")
        activeList = lists[name]

    elif cmd == "add":
        item = input("Enter Item: ")
        activeList.add(activelist, item)

    elif cmd == "list":
        activeList.display(activelist)
    elif cmd == "done":
        item = int(input("Which Item? "))
        activeList.done(activelist, item)
    elif cmd == "undo":
        item = int(input("Which Item? "))
        activeList.undo(activelist, item)
    elif cmd == "flush":
        activeList.flush(activelist)
    elif cmd == "exit":
        break
    else:
        print("Invalid Command. Please try from the given options")
