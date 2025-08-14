import add
import show
import update
import delete

add_task_reponse = add.add_task("sleep")
print(add_task_reponse)

show_tasks_response = show.show_tasks()
print(show_tasks_response)

update_task_response = update.update_tasks("sleep, wake up")
print(update_task_response)

delete_task_response = delete.delete_task("wake up")
print(delete_task_response)
