import saveload
import view
import user_interaction as ui
import edit

def start():
    ui.show("Приветствие!")
    notes = saveload.load_data()
    keep_going = True
    while keep_going:
        ui.show("\nВыберите действие:")
        ui.show("0. Просмотреть список заметок")
        ui.show("1. Просмотреть заметку")
        ui.show("2. Создать новую заметку")
        ui.show("3. Редактировать заметку")
        ui.show("4. Удалить заметку")
        ui.show("5. Выход")

        choice = ui.read("Желаемый номер действия: ")

        if choice == "0":
            view.show_all(notes)
        elif choice == "1":
            note_id = ui.read("Введите идентификатор заметки для просмотра: ")
            note = view.find_note(notes, note_id)
            if note:
                view.show_full_note(note)
            else:
                ui.show("Заметка с указанным идентификатором не найдена.")
        elif choice == "2":
            note = edit.create_note(notes)
            notes.append(note)
            saveload.save_data(notes)
            ui.show("Заметка создана успешно")
        elif choice == "3":
            note_id = ui.read("Введите идентификатор заметки для редактирования: ")
            note = view.find_note(notes, note_id)
            if note:
                edit.update_note(note)
                saveload.save_data(notes)
                ui.show("Заметка обновлена успешно")
            else:
                ui.show("Заметка с указанным идентификатором не найдена.")
        elif choice == "4":
            note_id = ui.read("Введите идентификатор заметки для удаления: ")
            if edit.delete_note(notes, note_id):
                saveload.save_data(notes)
                ui.show("Заметка успешно удалена")
            else:
                ui.show("Заметка с указанным идентификатором не найдена.")
        elif choice == "5":
            ui.show("Завершение работы программы.")
            keep_going = False
        else:
            ui.show("Ошибка выбора команды")
