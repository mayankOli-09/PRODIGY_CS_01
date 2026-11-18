<div align="center">

# 🔐 PixelGuard

#### ✨ Encrypt Images Like Magic — Pixel by Pixel ✨

**A fun and simple Python tool that encrypts and decrypts images using pixel manipulation.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-009688?style=for-the-badge&logo=pillow&logoColor=white)](https://python-pillow.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Fast%20Arrays-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-F9A825?style=for-the-badge)](#-license)

</div>

---

## 🌈 What is PixelGuard?

**PixelGuard** turns your normal image into a scrambled, encrypted version by changing pixel values and shuffling pixel positions.

Using the same secret key, you can decrypt the image and recover the original file perfectly.

> 🎨 **Encrypt. Decrypt. Repeat.**

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
|  **XOR Encryption** | Changes RGB pixel values using a secret key |
|  **Additive Encryption** | Adds a numeric key to every RGB channel |
|  **Pixel Shuffling** | Randomly rearranges pixel positions |
|  **Full Decryption** | Restores the original image exactly |
|  **PNG Support** | Saves lossless encrypted and decrypted images |
|  **Fast Processing** | Uses NumPy for efficient pixel operations |
|  **Simple CLI** | Easy-to-use command-line interface |

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-009688?style=for-the-badge&logo=pillow&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![PNG](https://img.shields.io/badge/Output-PNG-FF6F00?style=for-the-badge)

</div>

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/your-username/PixelGuard.git](https://github.com/your-username/PixelGuard.git)
cd PixelGuard
```

### 2️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Run the Tool

```bash
python image_encryptor.py
```

On macOS or Linux:

```bash
python3 image_encryptor.py
```

---

## 🎮 How to Use

### 🔒 Encrypt an Image

```text
Choose action - encrypt/decrypt: encrypt
Input image path: photo.jpg
Output image path (use .png): encrypted.png
Numeric key (0-255): 123
Operation - xor/add: xor
Shuffle pixel positions? (y/n): y
```

✅ Output:

```text
Encrypted image saved to: encrypted.png
```

### 🔓 Decrypt an Image

```text
Choose action - encrypt/decrypt: decrypt
Input image path: encrypted.png
Output image path (use .png): restored.png
Numeric key (0-255): 123
Operation - xor/add: xor
Shuffle pixel positions? (y/n): y
```

✅ Output:

```text
Decrypted image saved to: restored.png
```

> ⚠️ **Important:** Use the same key, operation, and shuffle setting for decryption.

---

## 🧠 How It Works

```text
 Original Image
        ↓
 Convert to RGB Pixel Array
        ↓
 Apply XOR / Addition
        ↓
 Shuffle Pixel Positions
        ↓
 Encrypted Image
```

### Decryption Flow

```text
 Encrypted Image
        ↓
 Reverse Pixel Shuffling
        ↓
 Reverse XOR / Addition
        ↓
 Original Image Restored
```

---

## Encryption Settings

| Setting | Example | Must Match? |
|--------|---------|-------------|
| Key | `123` | ✅ Yes |
| Operation | `xor` or `add` | ✅ Yes |
| Pixel Shuffling | `y` or `n` | ✅ Yes |
| Output Format | PNG | ✅ Recommended |

---

## Project Structure

```text
PixelGuard/
├── image_encryptor.py       # Main encryption tool
├── requirements.txt         # Dependencies
├── photo.jpg                # Sample image
├── encrypted.png            # Encrypted image
├── restored.png             # Decrypted image
└── README.md
```

---

## requirements.txt

```text
pillow
numpy
```

---

## ⚠️ Important Notes

- Always save encrypted and decrypted images as **PNG**
- Do not resize, crop, or recompress encrypted images
- Keep your encryption key safe
- This is an educational project, not military-grade encryption
- For real security, use AES or another trusted encryption method

---

## 🛣️ Future Improvements

- [ ] Add a graphical user interface  
- [ ] Encrypt multiple images at once  
- [ ] Generate keys from passwords  
- [ ] Add stronger encryption methods  
- [ ] Show before/after image preview  

---

## Contributing

Contributions are welcome!

1. Fork the project  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

---
<div align="center">

### Made with ❤️ using Python, Pillow & NumPy 

⭐ **Star this repo if you found it helpful!** ⭐

</div>
