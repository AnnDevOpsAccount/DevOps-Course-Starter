# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

### Values to add to local .env file (not stored in git - for security - so maintain a personal local copy):

* TRELLO_BOARD_KEY = "{key}"
* TRELLO_BOARD_TOKEN = "{token}"
* TRELLO_BOARD_ID = "{boardId}"
* TRELLO_TO_DO_LIST_ID = "{toDoListId}"
* TRELLO_DONE_LIST_ID = "{doneListId}"

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Student updated version:
GitPod URL for Ann's version of code:

https://gitpod.io/#https://github.com/AnnDevOpsAccount/DevOps-Course-Starter 

## Running the Unit Tests

Unit Tests are writtent in pytest - see: https://docs.pytest.org/en/6.2.x/index.html 


To run all tests, from command prompt:
`poetry run pytest`

To run specific test class from command promt (using relative path) - for 
example:
`pytest tests/test_view_mode.py`

Add -v for more verbose test output that is standard eg
`pytest tests/test_integration.py -v`

Also tests can be run in VSC IDE via Test explorer

## To provision a VM from an Ansible Control Node

`ansible-playbook to-do-app-playbook.yml -i inventory.ini`

-v can optionally be added for more verbose output

For Mod 4 this is in /home/ec2-user/to-do_app_setup on Ansible controller IP: 18.134.59.27 

## To view logs on managed server systemd task

`SSH onto the managed node |(for mod 4 = Managed node IP: 3.9.36.242 = ssh ec2-user@3.9.36.242  )` 

`$ journalctl -u todoapp`

## To view app running on managed server

view in browser at port 5000 of managed server for example:

`http://3.9.36.242:5000/`

## To Build Docker Container

`docker build --tag todo-app .`

## To Run Docker Container

`docker run --env-file ./.env -p 5000:5000 todo-app`
