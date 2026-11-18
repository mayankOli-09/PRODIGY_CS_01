import os
import numpy as np
from PIL import Image
def load_image_rgb(path):
    """Load an image as an RGB NumPy array."""
    with Image.open(path) as img:
        return np.array(img.convert("RGB"), dtype=np.uint8)
def save_image(array, path):
    """Save a NumPy RGB array as a lossless PNG image."""
    Image.fromarray(array, mode="RGB").save(path, format="PNG")
def xor_pixels(array, key):
    """XOR every RGB channel value with the key."""
    return np.bitwise_xor(array, np.uint8(key))
def add_pixels(array, key, decrypt=False):
    """Add or subtract a key modulo 256."""
    key = int(key) % 256
    if decrypt:
        return (array.astype(np.int16) - key).astype(np.uint8)
    return (array.astype(np.int16) + key).astype(np.uint8)
