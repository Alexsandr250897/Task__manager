FROM python:3.12
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | pip install -r /dev/stdin --no-deps
EXPOSE 8000
COPY ./entrypoint.sh ./
RUN chmod +x entrypoint.sh
COPY . ./
CMD ./entrypoint.sh && python manage.py runserver 0.0.0.0:8000