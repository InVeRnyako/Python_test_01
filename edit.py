import datetime
import json
import user_interaction as ui


def create_note(notes):
    note_id = get_unique_id(notes)
    note_title = ui.read("Введите заголовок заметки")
    note_body = ui.read("Введите содержимое заметки")
    note_created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "id" : note_id,
        "title" : note_title,
        "body" : note_body,
        "created_at" : note_created_at,
        "last_update" : note_created_at
    }


def update_note(note):
    title = ui.read("Введите новый заголовок:")
    body = ui.read("Введите новое содержимое:")
    note['title'] = title
    note['body'] = body
    note['last_update'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def delete_note(notes, note_id):
    for note in notes:
        if note['id'] == int(note_id):
            notes.remove(note)
            return True
    return False


def get_unique_id(data):
    ids = set()
    for item in data:
        if 'id' in item:
            ids.add(item['id'])

    new_unique_id = 0
    while new_unique_id in ids:
        new_unique_id += 1

    return new_unique_id
