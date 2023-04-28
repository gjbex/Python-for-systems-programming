from fastapi import FastAPI
from typing import Union

app = FastAPI()
stack = []

@app.get('/push/{value}')
def push(value: float, q: Union[str, None] = None):
    stack.append(value)

@app.get('/compute/{operator}')
def compute(operator: str, q: Union[str, None] = None):
    right_operand = stack.pop()
    left_operand = stack.pop()
    if operator == 'add':
        result = left_operand + right_operand
    elif operator == 'mult':
        result = left_operand*right_operand
    return {'result': result}
