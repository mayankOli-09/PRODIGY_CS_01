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


def get_permutation(array, key):
    """Create a deterministic pixel-position permutation from the key."""
    pixel_count = array.shape[0] * array.shape[1]
    rng = np.random.default_rng(key)
    return rng.permutation(pixel_count)
def swap_pixels(array, key, decrypt=False):
    """Shuffle pixel positions; use the inverse permutation to decrypt."""
    height, width, channels = array.shape
    flat = array.reshape(-1, channels)
    permutation = get_permutation(array, key)
    if decrypt:
        inverse = np.empty_like(permutation)
        inverse[permutation] = np.arange(len(permutation))
        flat = flat[inverse]
    else:
        flat = flat[permutation]
    return flat.reshape(height, width, channels)
def encrypt_image(input_path, output_path, key, use_xor=True, shuffle=True):
    array = load_image_rgb(input_path)
    if use_xor:
        array = xor_pixels(array, key)
    else:
        array = add_pixels(array, key, decrypt=False)
    if shuffle:
        array = swap_pixels(array, key, decrypt=False)
    save_image(array, output_path)
    print(f"Encrypted image saved to: {output_path}")
def decrypt_image(input_path, output_path, key, use_xor=True, shuffle=True):
    array = load_image_rgb(input_path)
    if shuffle:
        array = swap_pixels(array, key, decrypt=True)
    if use_xor:
        array = xor_pixels(array, key)
    else:
        array = add_pixels(array, key, decrypt=True)
    save_image(array, output_path)
    print(f"Decrypted image saved to: {output_path}")
