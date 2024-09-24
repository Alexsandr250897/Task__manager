Goal: Create a task management API where users can create, update, delete and get a list of tasks. Each task has a priority and a status. Tasks can be filtered by status, priority and creation date.

#### Functionality requirements:

1. Models:
- The Task model must contain the following fields:
- Task name (`title`, string)
- Task description (`description`, text)
- Task status (`status`, choice: new, in_progress, `completed`)
- Task priority (`priority`, choice: low, medium, `high`)
- Creation date (`created_at`, date)
- Updated date (`updated_at`, date)

- User model for managing users, a standard Django model.

2. API:
- POST /tasks/ — create a new task
- GET /tasks/ — get a list of all tasks, with the ability to filter by:
- Task status
- Priority
- Date created
- GET /tasks/{id}/ — get a task by ID
- PUT /tasks/{id}/ — update task information
- DELETE /tasks/{id}/ — delete a task

3. Filtering and pagination requirements:
- Implement the ability to filter by status, priority, and date created.
- Implement pagination of results.

4. Tests:
- Write unit tests for all API methods.
- Use pytest or standard Django tools for testing.

5. Authentication:
- Use Django Rest Framework (DRF) and token authentication (e.g. JWT).
6. Technical requirements:
- Use Django and Django REST Framework.
- Database: PostgreSQL or SQLite (depending on candidate preference).
- Code should be clean and understandable, with comments where necessary.
- Adhere to PEP8.

The project was implemented using a database PostgreSQL
and a library django-restframework
To launch this project, you need to screen the rupasitorium using command 
git clone https://github.com/Alexsandr250897/Task__manager.git
After cloning the repository, you need to run the command in the terminal
docker compose up --build
After executing this command, follow the link http://127.0.0.1:8000/api/