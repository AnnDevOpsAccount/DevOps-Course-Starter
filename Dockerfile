# base image
FROM python:3.7-buster

# poetry set up
ENV POETRY_HOME=${HOME}/.poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# copy across application code
COPY poetry.lock pyproject.toml todo_app ./
WORKDIR /todo_app
COPY ./todo_app /todo_app

# poetry install
RUN poetry install

# tell the port number the container should expose
EXPOSE 5000

# Define entrypoint 
ENTRYPOINT [ "poetry", "run", "gunicorn", "app:create_app()", "--bind", "0.0.0.0:5000" ]