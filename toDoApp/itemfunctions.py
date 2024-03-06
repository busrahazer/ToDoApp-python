# itemfunctions.py

def add_item(item_text, todo_list):
    todo_list.append(item_text)

def remove_item(index, todo_list):
    del todo_list[index]

def update_item(index, new_text, todo_list):
    todo_list[index] = new_text
