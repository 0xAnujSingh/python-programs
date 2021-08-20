x = ["apple", "banana", "mango"]


def add(item):
  x.append(item)
  print("item added")

def display():
  index = 0
  for i in x:
    print(index,i)
    index +=1

def done(idx):
  i = int(idx)
  item=x[i]
  done_item = "done" +" - "+ item
  x[i] = done_item
  display()

def flush():
  x.clear()
  print('flush')


## Interface
print("ToDo Application Commands List\n")
print("add: To add new item")
print("list: To display all items")
print("done: To mark an item as done")
print("flush: To flush the list")
print("exit: To close the application\n")

while True:
	cmd = input("Enter A Command: ")

	if (cmd == "add"):
		item = input("Enter Item: ")
		add(item)
	elif (cmd == "list"):
		display()
	elif (cmd == "done"):
		item = input("Which Item? ")
		done(item)
	elif (cmd == "flush"):
		flush()
	elif (cmd == "exit"):
		break
	else:
		print("Invalid Command. Please try from the given options")