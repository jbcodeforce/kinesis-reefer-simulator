FROM python
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

WORKDIR /app

RUN pip install --upgrade pip \
  && pip install pipenv boto3 flask gunicorn flasgger prometheus_client flask_restful

ADD . /app

EXPOSE 5000
CMD ["gunicorn", "-w 2", "-b 0.0.0.0:5000", "app:app"]
