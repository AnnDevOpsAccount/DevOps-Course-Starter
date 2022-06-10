# base image
FROM python:3.7-buster as base

# poetry set up
ENV POETRY_HOME=${HOME}/.poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

WORKDIR /myApp
COPY poetry.lock pyproject.toml ./

# copy across application code
COPY ./todo_app ./todo_app

# tell the port number the container should expose
EXPOSE 5000

#--- PRODUCTION SPECIFIC STEPS ----
FROM base as production

# poetry install, without dev dependencies
RUN poetry install --no-dev

# Define entrypoint 
ENTRYPOINT [ "poetry", "run", "gunicorn", "todo_app.app:create_app()", "--bind", "0.0.0.0:5000" ]

#--- DEVELOPMENT SPECIFIC STEPS ----
FROM base as development

# poetry install
RUN poetry install

# Define entrypoint 
ENTRYPOINT [ "poetry", "run", "flask", "run",  "--host", "0.0.0.0" ]