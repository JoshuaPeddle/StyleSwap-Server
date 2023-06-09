from PIL import Image
import tensorflow as tf
import io
from flask import  Request


def tensor_to_image(tensor):
    tensor = tf.cast(tf.clip_by_value(tensor, 0, 255), tf.uint8)
    image = Image.fromarray(tensor.numpy())
    byte_arr = io.BytesIO()
    image.save(byte_arr, format="JPEG")
    byte_arr.seek(0)
    return byte_arr


def crop_center(image):
    """Returns a cropped square image."""
    shape = image.shape
    new_shape = min(shape[1], shape[2])
    offset_y = max(shape[1] - shape[2], 0) // 2
    offset_x = max(shape[2] - shape[1], 0) // 2
    image = tf.image.crop_to_bounding_box(
        image, offset_y, offset_x, new_shape, new_shape
    )
    return image

def request_to_image(request: Request):
    image = request.files.get("image", False)
    if not image:
        image = request.files["image"]
    uuid = image.filename
    uuid = uuid[:-4]
    return Image.open(image), uuid
