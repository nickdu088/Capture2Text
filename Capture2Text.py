import mss
from PIL import Image
import datetime
import easyocr
import os

def capture_screen_text(left=None, top=None, width=None, height=None):
    """
    Capture a screen region (or full screen by default),
    perform OCR to extract text, and save both image and text.
    """
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Monitor 1 = primary screen
        screen_width = monitor['width']
        screen_height = monitor['height']

        # Set default full screen if region not specified
        if left is None:
            left = monitor['left']
        if top is None:
            top = monitor['top']
        if width is None:
            width = screen_width
        if height is None:
            height = screen_height

        region = {"top": top, "left": left, "width": width, "height": height}

        # Generate file names
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        image_path = f"screenshot_ocr_{timestamp}.png"
        text_path = f"screenshot_ocr_{timestamp}.txt"

        # Capture screenshot and save
        shot = sct.grab(region)
        img = Image.frombytes("RGB", shot.size, shot.rgb)
        img.save(image_path)
        print(f"Screenshot saved to: {image_path}")

    # Run OCR (English + Simplified Chinese)
    reader = easyocr.Reader(['ch_sim', 'en'])
    results = reader.readtext(image_path)

    # Extract text
    recognized_text = '\n'.join([res[1] for res in results])
    print("Recognized Text:")
    print("-" * 40)
    print(recognized_text)
    print("-" * 40)

    # Save OCR text
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(recognized_text)
    print(f"OCR text saved to: {text_path}")

if __name__ == "__main__":
    # Capture full screen by default
    # Use capture_screen_text(left=..., top=..., width=..., height=...) for a specific region
    capture_screen_text()
