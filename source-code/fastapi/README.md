# FastAPI

FastAPI is a nice framework to build web applications and handle http requests.

## What is it?

* `main.py`: very simple hello world application.
* `calculator.py`: implementation of an API that allows to
  * push numbers on a stack (push/<number>)
  * perform a computation (compute/add or compute/mult)
* `calculations.sh`: shell script to illustrate use of the calculator API.

## How to use it?

### Hello world application
```bash
$ uvicorn  main:app  --reload
```

### Calculator
```bash
$ uvicorn  calculatorapp  --reload
$ curl  --silent  http://127.0.0.1:8000/push/5
$ curl  --silent  http://127.0.0.1:8000/push/7
$ curl  --silent  http://127.0.0.1:8000/compute/add
```
