from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()


def text_response(response):
  return response.text.strip()

ip_services = {
  'https://checkip.amazonaws.com': text_response
}


@app.get("/")
def read_root():
  return { "Hello": "World" }

@app.get("/ip")
def get_external_ip():
    service = 'https://checkip.amazonaws.com'
    mapper_function = ip_services[service]
    ip = mapper_function(requests.get(service))
    return {"ip": ip}


if __name__ == '__main__':
  print(get_external_ip())
