from PIL import Image
from pytesseract import pytesseract
from dotenv import load_dotenv
import os

load_dotenv()

IMG_SAMPLE = os.getenv("SAMPLE_1")
PATH_TO_TESSERACT = os.getenv("PATH_TO_TESSERACT")

path_to_tesseract = PATH_TO_TESSERACT
image_path = IMG_SAMPLE

img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
print(text)