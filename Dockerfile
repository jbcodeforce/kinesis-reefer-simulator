FROM python:3.7.4-stretch
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

WORKDIR /app

RUN pip install --upgrade pip \
  && pip install pipenv boto3 flask gunicorn

COPY Pipfile .
COPY Pipfile.lock .
COPY requirements.txt .

# First we get the dependencies for the stack itself
RUN pipenv lock  > requirements.txt
RUN pip install -r requirements.txt


COPY . /app

EXPOSE 5000
CMD ["python", "app:reefer_simulator.py"]
