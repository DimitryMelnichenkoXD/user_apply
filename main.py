import functions_framework
from flask import Request
from google.rpc.http_pb2 import HttpResponse

from utilities.converter import image_to_byte
from utilities.generation_controller import GenerationController


@functions_framework.http
def user_apply(request: Request):
    generation_controller = GenerationController()
    image = generation_controller.image_generate()
    content = image_to_byte(image)
    headers = {"Content-Disposition": "attachment; filename={}".format("generated_image.png")}
    return HttpResponse(content, headers=headers)
