# Font-Identifier-Python
This project contains Python code for identifying the font used in a picture. It uses the Tesseract OCR library to extract text from an image and the WhatTheFont API to identify the font.
# Font Identifier

This project contains Python code for identifying the font used in a picture. It uses the Tesseract OCR library to extract text from an image and the WhatTheFont API to identify the font.

## Prerequisites

1. **Python**: Ensure you have Python installed on your system.
2. **Tesseract OCR**:
   - Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
   - Add Tesseract executable to your system's PATH.

## Setup

1. **Install Required Libraries**:
   ```sh
   pip install pytesseract pillow requests

2. **Configure Tesseract**:

Ensure Tesseract is installed and the executable is added to your PATH.
Set the path to the Tesseract executable in the code:

  ```sh
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
  ```

3. **Replace API Key**:
Sign up for the WhatTheFont API and get your API key.
Replace YOUR_API_KEY in the code with your actual API key.
Running the Program
Save the Python code to a file named font_identifier.py.

Run the Python script:
```sh
python font_identifier.py
```
>[!NOTE]
>Provide the path to the image file when prompted.


**Example**

If you run the script and provide the path to an image file, it will output something like:
  ```sh
  Enter the path to the image file: /path/to/image/file.jpg
  Extracted Text: Example Text
  Font identified: Arial by Monotype
```

>[!WARNING]
>  This code is protected by [MIT License](LICENSE).

