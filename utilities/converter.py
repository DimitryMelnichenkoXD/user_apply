import io


def image_to_byte(image):
    buf = io.BytesIO()
    image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im
