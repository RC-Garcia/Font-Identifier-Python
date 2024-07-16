# font_identifier.py
import pytesseract
from PIL import Image
import requests

# Set the path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Update with your path to tesseract

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def identify_font(image_path):
    api_url = "https://api.whatfontis.com/api/v1"  # Replace with actual API URL
    api_key = "YOUR_API_KEY"  # Replace with your API key

    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post(api_url, files=files, headers={'apikey': api_key})
    
    if response.status_code == 200:
        result = response.json()
        if result['fonts']:
            font = result['fonts'][0]
            return f"Font identified: {font['name']} by {font['foundry']}"
        else:
            return "Font could not be identified."
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    
    if not image_path:
        print("No file path provided.")
    else:
        text = extract_text(image_path)
        print(f"Extracted Text: {text}")
        font_info = identify_font(image_path)
        print(font_info)
