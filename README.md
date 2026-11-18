# 🔐 PixelGuard

<div align="center">

**A lightweight Python tool to encrypt and decrypt images using pixel manipulation**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-009688?logo=pillow&logoColor=white)](https://python-pillow.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Arrays-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-F9A825)](#-license)

</div>

---

## 📌 Overview

**PixelGuard** encrypts images by modifying RGB pixel values and rearranging pixel positions using a numeric key. The same key and settings can decrypt the image and restore it exactly.

It is a simple educational project for understanding image-level encryption concepts.

---

## ⚙️ Features

- 🔢 **XOR encryption** — modifies RGB channel values using a secret key  
- ➕ **Additive encryption** — shifts pixel values by a key amount  
- 🔀 **Pixel shuffling** — rearranges pixel positions deterministically  
- 🔁 **Exact decryption** — restores the original image with matching settings  
- 🖼️ **Lossless PNG output** — preserves pixel data during encryption and decryption  
- 💻 **Simple CLI** — no complex setup or configuration required  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or newer  
- pip package manager  

### Installation

```bash
git clone [https://github.com/your-username/PixelGuard.git](https://github.com/your-username/PixelGuard.git)
cd PixelGuard

python -m pip install -r requirements.txt
```

### Run

```bash
python image_encryptor.py
```

On macOS or Linux:

```bash
python3 image_encryptor.py
```

---

## 🖥️ Usage

### Encrypt an image

```text
Choose action - encrypt/decrypt: encrypt
Input image path: photo.jpg
Output image path (use .png): encrypted.png
Numeric key (0-255): 123
Operation - xor/add: xor
Shuffle pixel positions? (y/n): y
```

### Decrypt an image

```text
Choose action - encrypt/decrypt: decrypt
Input image path: encrypted.png
Output image path (use .png): restored.png
Numeric key (0-255): 123
Operation - xor/add: xor
Shuffle pixel positions? (y/n): y
```

> ⚠️ Use the **same key, operation, and shuffle setting** used during encryption.

---

## 🧠 How It Works

```text
Original Image
      ↓
RGB Pixel Array
      ↓
XOR / Add Pixel Values
      ↓
Shuffle Pixel Positions
      ↓
Encrypted PNG
```

Decryption reverses the pixel shuffling and pixel-value operation.

### XOR Example

\[
c = p \oplus k
\]

\[
p = c \oplus k
\]

Where:

- `p` = original pixel value  
- `c` = encrypted pixel value  
- `k` = secret key  

---

## 📁 Project Structure

```text
PixelGuard/
├── image_encryptor.py     # Main program
├── requirements.txt       # Dependencies
├── photo.jpg              # Sample input image
├── encrypted.png          # Encrypted output
├── restored.png           # Decrypted output
└── README.md
```

---

## 📦 requirements.txt

```text
pillow
numpy
```

---

## ⚠️ Notes

- Save encrypted and decrypted files as **PNG**, not JPEG.
- Do not resize, crop, or recompress the encrypted image.
- This project is for educational purposes and is **not production-grade cryptography**.
- For sensitive data, use established encryption such as AES.

---

## 🛣️ Future Improvements

- [ ] Add a graphical user interface  
- [ ] Support batch image encryption  
- [ ] Generate keys from passwords  
- [ ] Add stronger encryption methods  
- [ ] Include before/after image previews  

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

Made with ❤️ using **Python, Pillow, and NumPy**

</div>
