import user_interaction as ui


def show_all(notes):
    for note in notes:
        ui.show(f"ID: {note['id']}")
        ui.show(f"Заголовок: {note['title']}")
        ui.show(f"Создано: {note['created_at']}")
        ui.show(f"Обновлено: {note['last_update']}")
        ui.show("-------")


def find_note(notes, note_id):
    for note in notes:
        if note['id'] == int(note_id):
            return note
    return None


def show_full_note(note):
    ui.show(f"ID: {note['id']}")
    ui.show(f"Заголовок: {note['title']}")
    ui.show(f"Содержимое заметки: {note['body']}")
    ui.show(f"Создано: {note['created_at']}")
    ui.show(f"Обновлено: {note['last_update']}")
    ui.show("-------")
