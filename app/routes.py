from app import app
from fake_data.tasks import tasks_list

@app.route('/')
def index():
    first_name = 'Nathaniel'
    last_name = 'Godfrey'
    return f'Hello World!! - From {first_name} {last_name}, now go find tasks to do!'


@app.route('/tasks')
def get_tasks():
    tasks = tasks_list
    return tasks

@app.route('/tasks/<int:tasks_id>')
def get_task(tasks_id):
    tasks = tasks_list
    for task in tasks:
        if task['id'] == tasks_id:
            return task
    return {'error': f'Task with an ID of {tasks_id} does not exist'}, 404