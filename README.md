🔐 PixelGuard — Image Encryption with Pixel Manipulation
<div align="center">

Encrypt and decrypt images using reversible pixel transformations

Pixel Manipulation - XOR Encryption - Pixel Shuffling - Python + Pillow

[
[
[
[

</div>

🎯 What is PixelGuard?
PixelGuard is a simple Python image-encryption tool that protects images by changing both their pixel values and pixel positions. It uses a numeric key to apply reversible operations, allowing the original image to be restored exactly with the same settings.

It is designed as an educational project for learning how image data can be manipulated at the pixel level.

✨ Key Features
Feature	Description
1. XOR Pixel Encryption	XORs each RGB channel value with a user-provided key
2. Additive Encryption	Adds a key value to every RGB channel, with modulo-256 wrapping
3. Pixel Position Shuffling	Randomly rearranges pixel positions using a key-based permutation
4. Full Decryption Support	Restores the original image using the same key and settings
5. PNG Output	Saves encrypted and decrypted images losslessly as PNG files
6. Fast Processing	Uses NumPy arrays for efficient whole-image pixel operations
7. Quick Start
Prerequisites
Make sure you have installed:

Python 3.8+

pip

Pillow

NumPy

Setup & Run
bash
# 1. Clone the repository
git clone https://github.com/your-username/PixelGuard.git
cd PixelGuard

# 2. Install dependencies
python -m pip install --upgrade pip
python -m pip install pillow numpy

# 3. Run the application
python image_encryptor.py
On macOS or Linux, use python3 if python is not available:

bash
python3 image_encryptor.py
Python runs a saved script with the command python script_name.py; Pillow can be installed through pip.

🖥️ How to Use
When the program starts, follow the prompts:

text
Pixel Manipulation Image Encryption
----------------------------------
Choose action - encrypt/decrypt:
Encrypt an image
text
Choose action - encrypt/decrypt: encrypt
Input image path: photo.jpg
Output image path (use .png): encrypted.png
Numeric key (0-255): 123
Operation - xor/add: xor
Shuffle pixel positions? (y/n): y
Output:

text
Encrypted image saved to: encrypted.png
Decrypt an image
Run the program again and use the same key and settings:

text
Choose action - encrypt/decrypt: decrypt
Input image path: encrypted.png
Output image path (use .png): restored.png
Numeric key (0-255): 123
Operation - xor/add: xor
Shuffle pixel positions? (y/n): y
Output:

text
Decrypted image saved to: restored.png
🔑 Encryption Settings
Setting	Example	Must match during decryption?
Action	encrypt / decrypt	Yes
Input image	encrypted.png	Yes
Output image	restored.png	No
Numeric key	123	Yes
Operation	xor or add	Yes
Pixel shuffling	y or n	Yes
⚠️ Keep your key safe. If the key, operation, or shuffle setting changes, the image cannot be restored correctly.

🧠 How It Works
text
Original image
        ↓
Convert image to RGB pixel array
        ↓
Apply XOR or addition to pixel values
        ↓
Shuffle pixel positions using a key-based permutation
        ↓
Save encrypted PNG image
For decryption, the process is reversed:

text
Encrypted image
        ↓
Apply inverse pixel-position permutation
        ↓
Reverse XOR or addition operation
        ↓
Save restored PNG image
XOR example
For a pixel channel value p and key k:

𝑐
=
𝑝
⊕
𝑘
c=p⊕k
To decrypt:

𝑝
=
𝑐
⊕
𝑘
p=c⊕k
Because XOR is reversible, applying the same key twice restores the original value.

🏗️ Project Structure
text
PixelGuard/
├── image_encryptor.py       # Main encryption and decryption program
├── photo.jpg                # Example input image
├── encrypted.png            # Encrypted output image
├── restored.png             # Decrypted output image
├── requirements.txt         # Python dependencies
└── README.md
📦 requirements.txt
Create a file named requirements.txt with:

text
pillow
numpy
Then install everything with:

bash
python -m pip install -r requirements.txt
🛠️ Tech Stack
Layer	Technology
Language	Python 3.8+
Image Processing	Pillow
Pixel Operations	NumPy
Output Format	PNG
Interface	Command-line interface
⚠️ Important Notes
Use PNG for encrypted and decrypted output files. JPEG compression can change pixel values and prevent exact restoration.

The image dimensions must remain unchanged between encryption and decryption.

This project is intended for learning and demonstration, not for securing highly sensitive images.

For real-world security, use a trusted cryptographic library and a standard algorithm such as AES.

🧪 Example Workflow
bash
# Encrypt
python image_encryptor.py
# Choose: encrypt
# Input: photo.jpg
# Output: encrypted.png
# Key: 123
# Operation: xor
# Shuffle: y

# Decrypt
python image_encryptor.py
# Choose: decrypt
# Input: encrypted.png
# Output: restored.png
# Key: 123
# Operation: xor
# Shuffle: y
🤝 Contributing
Contributions are welcome. You can improve the project by adding:

A graphical user interface using Tkinter or Streamlit

Batch encryption for multiple images

Password-based key generation

Stronger cryptographic methods

Image preview before and after encryption

📄 License
This project is released under the MIT License.

<div align="center">

Built with ❤️ using Python, Pillow, and NumPy
⭐ Star this repository if it helped you learn image encryption!

</div>
