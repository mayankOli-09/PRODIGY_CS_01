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

def main():
    print("Pixel Manipulation Image Encryption")
    print("----------------------------------")
    action = input("Choose action - encrypt/decrypt: ").strip().lower()
    if action not in ("encrypt", "decrypt"):
        print("Invalid action.")
        return
    input_path = input("Input image path: ").strip()
    output_path = input("Output image path (use .png): ").strip()
    try:
        key = int(input("Numeric key (0-255): "))
        if not 0 <= key <= 255:
            raise ValueError
    except ValueError:
        print("Key must be an integer from 0 to 255.")
        return
    operation = input("Operation - xor/add: ").strip().lower()
    use_xor = operation == "xor"
    if operation not in ("xor", "add"):
        print("Invalid operation.")
        return
    shuffle_input = input("Shuffle pixel positions? (y/n): ").strip().lower()
    shuffle = shuffle_input == "y"
    if not os.path.exists(input_path):
        print("Input image not found.")
        return
    if action == "encrypt":
        encrypt_image(input_path, output_path, key, use_xor, shuffle)
    else:
        decrypt_image(input_path, output_path, key, use_xor, shuffle)
if __name__ == "__main__":
    main()
