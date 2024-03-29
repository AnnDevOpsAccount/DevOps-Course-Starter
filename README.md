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

* MONGO_CONNECTION_STRING={mongoConnectionString}
* MONGO_DATABASE={mongoDatabase}

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
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app. <br>
<br>

# Ann's additions:
GitPod URL for Ann's version of code:

https://gitpod.io/#https://github.com/AnnDevOpsAccount/DevOps-Course-Starter <br>
<br>

# Running the Unit Tests (Module 3)

Unit Tests are writtent in pytest - see: https://docs.pytest.org/en/6.2.x/index.html 


To run all tests, from command prompt:
`poetry run pytest`

To run specific test class from command promt (using relative path) - for 
example:
`pytest tests/test_view_mode.py`

Add -v for more verbose test output that is standard eg
`pytest tests/test_integration.py -v`

Also tests can be run in VSC IDE via Test explorer <br>
<br>

# Working With Ansible (Module 4)
## To provision a VM from an Ansible Control Node

`ansible-playbook to-do-app-playbook.yml -i inventory.ini`

-v can optionally be added for more verbose output

For Mod 4 this is in /home/ec2-user/to-do_app_setup on Ansible controller IP: 18.134.59.27 

## To view logs on managed server systemd task

`SSH onto the managed node |(for mod 4 = Managed node IP: 3.9.36.242 = ssh ec2-user@3.9.36.242  )` 

`$ journalctl -u todoapp`

## To view app running on managed server

view in browser at port 5000 of managed server for example:

`http://3.9.36.242:5000/`<br>
<br>


# Working With Docker (Modules 5 & 7)

## To build Docker Container
```
# multi-stage versions
docker build --target production --tag todo-app:prod .
docker build --target development --tag todo-app:dev .
docker build --target test --tag todo-app:test .
```
## To run Docker Container
```
# dev version
docker run --env-file ./.env -p 5000:5000 todo-app:dev

# prod version
docker run --env-file ./.env -p 5000:5000 todo-app:prod

# test version
docker run --env-file ./.env.test todo-app:test
```

#### **Dev** multi-stage version, with a **bind mount** to pick up code changes as they happen:
```
docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,destination=/myApp/todo_app todo-app:dev
```
#### to run detatched add **-d** eg:
```
docker run --env-file ./.env -d -p 5000:5000 todo-app
```

#### and then to view logs, of detatched running container:
```
docker logs {CONTAINER}
eg: docker logs frosty_bartik
```
## To stop Docker Container
```
docker stop {CONTAINER}
eg docker stop frosty_bartik
```

# Architecture Diagrams (Module 6)

See the documentation folder

The diagrams are saved as .jpg files, named per level of The C4 Model - as per https://c4model.com/ 

The source code for these is in same named .drawio files and can be edited using https://app.diagrams.net/

NOTE - these are yet to be updated for the switch from storing tasks in Trello to storing them in mongo DB on Azure 

# Continuous Integration (Module 7)

## To run the tests from docker
```
docker run --env-file ./.env.test todo-app:test
```
## github workflow file 

### ...was created to run the unit tests: 

See the .yml file which stored at below location, which dictates the pipelines that run on GitHub to test every branch
```
.github/workflows/
```
# Continuous Delivery (Module 8)

The GitHub actions workflow file ( .github/workflows/ci-and-cd-pipeline.yml ) was enhanced to provide continuous deployment to **Heroku** hosting platform, using an image pushed to **Docker Hub** but the use of Heroku was removed in module 9, when the app was re-platformed onto Azure.

# Cloud Infrastructure (Module 9)
### Continuous deployment
The GitHub actions workflow file ( .github/workflows/ci-and-cd-pipeline.yml ) now provides continuous deployment to **Azure** hosting platform, using the latest prod image pushed to **Docker Hub**.
This deployment is conditional upon:
1) the git action is a pull or push
2) project built and tests passed
3) target is main branch or module9/module10 branch

### Secrets:
Secrets have been stored in
#### 1) the **GitHub repository** :
* Docker Hub signon - used to publish updated app
* Azure Webhook url - used to trigger Arure to collect and load updated app version 

These secrets are only available to the GitHub repository owner, not to others who it is shared with.
### 2) the **App within Azure** to store env values of:
* mongo DB / Azure database access info
* app port number (5000)


### URI to access the deployed app: 
  https://annd0409devopstodoapp.azurewebsites.net

### GitHub Actions Logs:
can be viewed at https://github.com/AnnDevOpsAccount/DevOps-Course-Starter/actions

# Data and Security I (Module 10)
Amended the app to use mongo DB on Azure, instead of Trello API, for store/retrieve to-do task info 
