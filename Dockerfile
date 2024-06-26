FROM python:3.12-alpine
WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
RUN pip install --no-cache-dir -r /api/requirements.txt
COPY ./ipchecker/ /api/
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
