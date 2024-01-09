from app import app
from fake_data.tasks import tasks_list

@app.route('/')
def index():
    first_name = 'Nathaniel'
    last_name = 'Godfrey'
    return f'Hello World!! - From {first_name} {last_name}, now go find tasks to do!'


# POST ENDPOINTS

# Get all posts
@app.route('/tasks')
def get_tasks():
    # Get the posts from storage (fake data, will setup db tomorrow)
    tasks = tasks_list
    return tasks

# Get single post by ID
@app.route('/tasks/<int:tasks_id>')
def get_task(tasks_id):
    # Get the posts from storage
    tasks = tasks_list
    # For each dictionary in the list of post dictionaries
    for task in tasks:
        # if the key of 'id' on the post dictionary matches the post_id from the URL
        if task['id'] == tasks_id:
            # Return that post dictionary
            return task
    # If we loop through all of the posts without returning, the post with that ID does not exist
    return {'error': f'Task with an ID of {tasks_id} does not exist'}, 404