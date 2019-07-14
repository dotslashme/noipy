FROM python:3-alpine

COPY noipy.py /

RUN pip install --no-cache-dir requests

CMD ["python", "/noipy.py"]