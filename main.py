import functions_framework
from flask import Request

from utilities.converter import image_to_byte
from utilities.generation_controller import GenerationController
from google.cloud.functions import HttpResponse


@functions_framework.http
def user_apply(request: Request):
    generation_controller = GenerationController()
    image = generation_controller.image_generate()
    content = image_to_byte(image)
    headers = {"Content-Disposition": "attachment; filename={}".format("generated_image.png")}
    return HttpResponse(content, headers=headers)
