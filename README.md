# 📸 Screenshot OCR App (Python)

A cross-platform Python utility to **capture screenshots** of any region on your screen and perform **OCR (Optical Character Recognition)** to extract text from images. Works on **Windows**, **Linux**, and **macOS**.

---

## ✅ Features

- 🖥️ Capture any part of the screen (or the full screen by default)
- 🔍 Extract text from images using OCR
- 🌐 Supports English and Simplified Chinese (🇬🇧 🇨🇳)
- 💾 Automatically saves screenshot and recognized text
- ⚙️ Easy to customize or extend

---

## 📦 Requirements

- Python 3.7+
- [easyocr](https://github.com/JaidedAI/EasyOCR)
- [mss](https://github.com/BoboTiG/python-mss)
- [Pillow](https://pypi.org/project/Pillow/)

### 🔧 Installation

```bash
pip install easyocr mss pillow

On Linux, you may need libgl1:
```bash
sudo apt install libgl1
```

## 🚀 Usage

### ▶️ Run the script

```bash
python screenshot_ocr.py
```
By default, it captures the entire screen.


## 🙌 Credits

### [EasyOCR](https://github.com/JaidedAI/EasyOCR)
### [MSS (multi-screen-shot)](https://github.com/BoboTiG/python-mss)
### [Pillow (PIL)](https://pypi.org/project/Pillow/)
