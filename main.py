from flask import Request
import functions_framework
from models.input.in_user_apply import InUserApply


@functions_framework.http
def user_apply(request: Request):
    return InUserApply(**request.get_json()).dict()
